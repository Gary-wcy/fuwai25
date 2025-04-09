import cv2
import numpy as np
import time
import concurrent.futures
import os


def highlight_human_regions_from_fused(fused_image, thermal_path, output_size=(640, 360)):
    """处理已融合图像和热成像图，执行人体检测和上色操作"""
    # 1. 图像预处理
    if isinstance(fused_image, str):  # 如果传入的是路径
        fused_image = cv2.resize(cv2.imread(fused_image), output_size)
    else:  # 否则假设已经是图像对象
        fused_image = cv2.resize(fused_image, output_size)

    thermal = cv2.resize(cv2.imread(thermal_path, 0), output_size)
    start_time = time.time()

    # 2. 热成像增强（优化CLAHE参数）
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    thermal_enhanced = clahe.apply(thermal)

    # 3. 多级阈值计算
    mean_val = np.mean(thermal_enhanced)
    std_val = np.std(thermal_enhanced)
    threshold_high = min(255, mean_val + 1.8 * std_val)
    threshold_extreme = min(255, mean_val + 3.0 * std_val)

    # 4. 生成掩码
    _, high_mask = cv2.threshold(thermal_enhanced, threshold_high, 255, cv2.THRESH_BINARY)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    high_mask = cv2.morphologyEx(high_mask, cv2.MORPH_CLOSE, kernel)
    high_mask = cv2.morphologyEx(high_mask, cv2.MORPH_OPEN, kernel)

    # 5. 人体区域分析 - 增强人体检测
    contours, _ = cv2.findContours(high_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    human_mask = np.zeros_like(high_mask)
    extreme_mask = (thermal_enhanced > threshold_extreme).astype(np.uint8) * 255

    # 增加一个辅助区域掩码，用于捕获可能的人体区域
    potential_human_mask = np.zeros_like(high_mask)

    # 新增：用于人形识别的掩码
    human_shape_mask = np.zeros_like(high_mask)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 600: continue  # 略微降低面积阈值

        # 添加：针对小目标（如安全出口）的额外检查
        if area < 350:  # 较小的目标需要额外检查
            x, y, w, h = cv2.boundingRect(cnt)

            # 计算实心度 - 轮廓面积与其凸包面积的比率
            # 安全出口通常具有较高的实心度（非常紧凑）
            hull = cv2.convexHull(cnt)
            hull_area = cv2.contourArea(hull)
            solidity = float(area) / hull_area if hull_area > 0 else 0

            # 计算强度指标
            contour_mask = np.zeros_like(thermal_enhanced)
            cv2.drawContours(contour_mask, [cnt], -1, 255, -1)

            # 获取区域的平均强度
            region_pixels = cv2.bitwise_and(thermal_enhanced, thermal_enhanced, mask=contour_mask)
            mean_intensity = np.mean(region_pixels[contour_mask > 0]) if np.any(contour_mask > 0) else 0

            # 安全出口通常具有以下特征:
            # 1. 较小
            # 2. 非常亮（高强度）
            # 3. 紧凑（高实心度）
            # 4. 通常有规则形状（正方形出口的宽高比接近1）
            if (solidity > 0.85 and  # 非常紧凑
                    mean_intensity > threshold_extreme * 0.9 and  # 非常亮
                    (0.5 < w / h < 2.0)):  # 较为方正
                continue  # 跳过这个区域 - 可能是安全出口或类似的小物体

        # 快速形状判断
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = max(w, h) / (min(w, h) + 1e-5)
        if aspect_ratio > 3.6: continue

        # 计算轮廓的更多特征 - 新增：检测人形特征
        perimeter = cv2.arcLength(cnt, True)
        compactness = (perimeter * perimeter) / (4 * np.pi * area + 1e-5)

        # 新增：检查是否为典型人形
        is_human_shape = False
        if (1.5 < h / w < 4.0 and  # 人通常更高而不是更宽
                area > 800 and  # 人体区域通常较大
                compactness < 3.5 and  # 人体轮廓相对规则
                w >= 20):  # 人的宽度通常不会太窄
            is_human_shape = True
            cv2.drawContours(human_shape_mask, [cnt], -1, 255, -1)

        # 专门针对竖直烟雾的检测 - 修改为更精确的判别
        # 烟雾通常非常细长且宽度较小，而站立的人则宽度较大
        # 只有当区域非常窄且高时才认为是烟雾
        is_smoke = False
        if h > 3 * w:  # 竖直细长物体
            if w < 20 and h > 80:  # 原来的条件
                # 进一步分析形状特征来区分人和烟
                # 计算轮廓的紧凑度
                if compactness > 3.0 and w < 15:  # 烟雾具有高度不规则形状且非常窄
                    is_smoke = True

        if is_smoke:
            continue  # 跳过确认为烟雾的区域

        # 极高温区域检测
        contour_mask = np.zeros_like(extreme_mask)
        cv2.drawContours(contour_mask, [cnt], -1, 255, -1)
        extreme_ratio = np.sum(extreme_mask & contour_mask) / (area * 255 + 1e-5)

        # 判断是否是人体的规则 - 增强版
        is_human = False

        # 基本判断条件：极高温比例较低
        if extreme_ratio < 0.5:
            is_human = True
        # 新增：如果已被识别为人形，放宽温度限制
        elif is_human_shape and extreme_ratio < 0.9:
            is_human = True
        # 针对站立人体的额外判断：竖直较高但宽度合适
        elif h > 2.5 * w and w >= 20 and extreme_ratio < 0.65:
            is_human = True
        # 捕获可能是人体但极高温比例略高的边缘情况
        elif extreme_ratio < 0.62 and area > 300 and aspect_ratio < 2.0:
            cv2.drawContours(potential_human_mask, [cnt], -1, 255, -1)

        # 如果判断为人体，添加到人体掩码
        if is_human:
            cv2.drawContours(human_mask, [cnt], -1, 255, -1)

    # 6. 掩码优化与增强

    # 先进行人体掩码的膨胀，确保完整覆盖人体
    human_mask = cv2.dilate(human_mask, kernel, iterations=1)

    # 处理潜在人体区域
    combined_mask = human_mask.copy()
    if np.sum(potential_human_mask) > 0:  # 如果存在潜在人体区域
        # 轻微膨胀潜在区域，以便与确认的人体区域连接
        potential_dilated = cv2.dilate(potential_human_mask, kernel, iterations=2)

        # 检查是否有任何潜在区域与确认的人体区域相交
        overlap = cv2.bitwise_and(potential_dilated, human_mask)
        if np.sum(overlap) > 0:  # 如果有重叠
            # 将这些潜在区域添加到人体掩码中
            combined_mask = cv2.bitwise_or(human_mask, potential_human_mask)
        else:
            # 即使没有重叠，也检查是否有大面积的潜在人体区域（可能是孤立的人体）
            # 找出潜在人体区域的连通组件
            num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(potential_human_mask)
            for i in range(1, num_labels):  # 跳过背景
                component_area = stats[i, cv2.CC_STAT_AREA]
                component_width = stats[i, cv2.CC_STAT_WIDTH]
                component_height = stats[i, cv2.CC_STAT_HEIGHT]

                # 如果连通区域足够大，或者具有类似人体的比例，则保留它
                if (component_area > 400 or
                        (component_height > 2 * component_width and component_width >= 20 and component_height >= 60)):
                    # 创建该连通区域的掩码
                    component_mask = np.zeros_like(potential_human_mask)
                    component_mask[labels == i] = 255
                    # 添加到组合掩码
                    combined_mask = cv2.bitwise_or(combined_mask, component_mask)

    # 新增：合并可能的人形区域
    if np.sum(human_shape_mask) > 0:
        combined_mask = cv2.bitwise_or(combined_mask, human_shape_mask)

    # 最终的人体掩码
    human_mask = combined_mask

    # 7. 热力图颜色处理
    human_heat = cv2.applyColorMap(cv2.bitwise_and(thermal_enhanced, thermal_enhanced, mask=human_mask),
                                   cv2.COLORMAP_HOT)
    non_human_heat = cv2.applyColorMap(cv2.bitwise_and(thermal_enhanced, thermal_enhanced, mask=high_mask - human_mask),
                                       cv2.COLORMAP_OCEAN)

    # 8. 将热力图应用到已融合图像上
    colored = cv2.cvtColor(fused_image, cv2.COLOR_BGR2GRAY)
    colored = cv2.cvtColor(colored, cv2.COLOR_GRAY2BGR)
    colored = cv2.addWeighted(colored, 0.7, human_heat, 0.3, 0)
    colored = cv2.addWeighted(colored, 0.92, non_human_heat, 0.08, 0)

    # 9. 亮度增强
    hsv = cv2.cvtColor(colored, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = np.clip(v.astype(np.float32) * 1.3, 0, 255).astype(np.uint8)
    hsv = cv2.merge([h, s, v])
    colored = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    print(f"处理耗时: {time.time() - start_time:.2f}s")
    return colored, human_mask


def generate_heatmap(thermal_enhanced, human_mask, non_human_mask):
    """并行生成热力图"""
    human_heat = cv2.applyColorMap(cv2.bitwise_and(thermal_enhanced, thermal_enhanced, mask=human_mask),
                                   cv2.COLORMAP_HOT)
    non_human_heat = cv2.applyColorMap(cv2.bitwise_and(thermal_enhanced, thermal_enhanced, mask=non_human_mask),
                                       cv2.COLORMAP_OCEAN)
    return human_heat, non_human_heat


def adjust_human_visibility(img):
    """可见性增强（直接处理内存数据）"""
    start_time = time.time()

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    s = np.clip(s.astype(np.float32) * 1.85, 0, 255).astype(np.uint8)
    v = np.clip(v.astype(np.float32) * 1.4, 0, 255).astype(np.uint8)

    hsv = cv2.merge([h, s, v])
    end_time = time.time()
    print(f"adjust_human_visibility 耗时: {end_time - start_time:.4f}s")
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


def adjust_for_fire_detection(img, human_mask):
    """火焰抑制（直接处理内存数据）- 增强版，避免将人体误识别为火"""
    start_time = time.time()

    # 火焰颜色检测
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, np.array([0, 150, 100]), np.array([10, 255, 255]))
    mask2 = cv2.inRange(hsv, np.array([160, 150, 100]), np.array([180, 255, 255]))
    fire_mask = cv2.bitwise_or(mask1, mask2)

    # 形态学操作
    kernel = np.ones((5, 5), np.uint8)
    fire_mask = cv2.morphologyEx(fire_mask, cv2.MORPH_CLOSE, kernel)

    # 新增：增强人体掩码以确保人不被识别为火
    dilated_human_mask = cv2.dilate(human_mask, kernel, iterations=2)

    # 确保火焰掩码不包含人体区域
    fire_mask = cv2.bitwise_and(fire_mask, cv2.bitwise_not(dilated_human_mask))

    # 新增：额外检查可能的人形区域
    # 获取火焰区域的轮廓
    fire_contours, _ = cv2.findContours(fire_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in fire_contours:
        area = cv2.contourArea(cnt)
        if area < 500: continue  # 忽略小区域

        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = h / (w + 1e-5)

        # 如果区域有类似人形的特征 (高大且不太宽)
        if aspect_ratio > 1.8 and h > 70 and w > 18 and w < h / 2:
            # 这可能是一个人，从火焰掩码中移除
            temp_mask = np.zeros_like(fire_mask)
            cv2.drawContours(temp_mask, [cnt], -1, 255, -1)
            fire_mask = cv2.bitwise_and(fire_mask, cv2.bitwise_not(temp_mask))

    # 颜色修正（添加安全检查）
    corrected = img.copy()
    fire_pixels = np.where(fire_mask > 0)
    if len(fire_pixels[0]) > 0:  # 如果存在火焰区域
        blue_purple = np.full_like(img, (150, 30, 80))
        corrected[fire_pixels] = cv2.addWeighted(
            img[fire_pixels], 0.5,
            blue_purple[fire_pixels], 0.5, 0
        )

    end_time = time.time()
    print(f"adjust_for_fire_detection 耗时: {end_time - start_time:.4f}s")
    return corrected


def adjust_exposure(img, target_brightness=127, tolerance=15):
    """
    自动曝光调整函数，根据图像亮度与目标值的差异调整曝光

    参数:
    img - 输入图像
    target_brightness - 目标亮度值 (0-255)
    tolerance - 允许偏差，在这个范围内不调整 (0-255)

    返回:
    调整后的图像
    """
    start_time = time.time()

    # 计算当前亮度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    current_brightness = np.mean(gray)

    # 如果亮度在允许范围内，则不调整
    if abs(current_brightness - target_brightness) <= tolerance:
        print(f"亮度正常 ({current_brightness:.1f})，不需调整")
        return img

    # 计算调整系数
    if current_brightness < target_brightness - tolerance:  # 图像过暗
        alpha = min(2.0, target_brightness / max(1, current_brightness))  # 限制最大增益
        beta = min(30, target_brightness - current_brightness) / 2  # 轻微提升基础亮度
        print(f"图像过暗 ({current_brightness:.1f})，增加曝光 (α={alpha:.2f}, β={beta:.1f})")
    elif current_brightness > target_brightness + tolerance:  # 图像过亮
        alpha = max(0.5, target_brightness / max(1, current_brightness))  # 限制最低增益
        beta = max(-30, target_brightness - current_brightness) / 2  # 轻微降低基础亮度
        print(f"图像过亮 ({current_brightness:.1f})，降低曝光 (α={alpha:.2f}, β={beta:.1f})")
    else:
        return img  # 正常范围内不调整

    # 应用亮度调整
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    end_time = time.time()
    print(f"adjust_exposure 耗时: {end_time - start_time:.4f}s")
    return adjusted


def process_image_pair(fused_path, thermal_path, output_dir, target_brightness=127, tolerance=15):
    """处理已融合的图像和热成像图像并保存结果"""
    try:
        # 加载融合图像
        fused_image = cv2.imread(fused_path)

        # 首先进行曝光调整 - 修改: 曝光调整移到了人体检测和上色之前
        exposure_adjusted = adjust_exposure(fused_image, target_brightness, tolerance)

        # 处理图像 - 传入调整后的图像给人体检测函数
        colored, human_mask = highlight_human_regions_from_fused(exposure_adjusted, thermal_path)
        enhanced_colored = adjust_human_visibility(colored)
        fire_suppressed = adjust_for_fire_detection(enhanced_colored, human_mask)

        # 保存结果
        filename = os.path.basename(fused_path)
        output_path = os.path.join(output_dir, filename)
        cv2.imwrite(output_path, fire_suppressed)
        return True, filename
    except Exception as e:
        print(f"处理 {os.path.basename(fused_path)} 时出错: {str(e)}")
        return False, os.path.basename(fused_path)


if __name__ == "__main__":
    total_start = time.time()

    # 配置路径
    FUSED_DIR = "all"  # 已融合图像目录
    THERMAL_DIR = "images-rcx"  # 热成像图像目录
    OUTPUT_DIR = "images-result1.4.2"  # 输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 设置曝光调整参数（可调整）
    TARGET_BRIGHTNESS = 101  # 目标亮度值(0-255)，中间值为127
    TOLERANCE = 5  # 允许的亮度偏差范围

    print(f"自动曝光参数：目标亮度={TARGET_BRIGHTNESS}，容差范围=±{TOLERANCE}")

    # 获取匹配的文件列表
    valid_extensions = {'.jpg', '.jpeg', '.png', '.bmp'}
    fused_files = {f for f in os.listdir(FUSED_DIR)
                   if os.path.splitext(f)[1].lower() in valid_extensions}
    thermal_files = {f for f in os.listdir(THERMAL_DIR)
                     if os.path.splitext(f)[1].lower() in valid_extensions}
    common_files = sorted(fused_files & thermal_files)

    print(f"发现 {len(common_files)} 对需要处理的图像")

    # 使用线程池并行处理
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for filename in common_files:
            fused_path = os.path.join(FUSED_DIR, filename)
            thermal_path = os.path.join(THERMAL_DIR, filename)
            futures.append(executor.submit(
                process_image_pair,
                fused_path,
                thermal_path,
                OUTPUT_DIR,
                TARGET_BRIGHTNESS,
                TOLERANCE
            ))

        # 处理完成统计
        success_count = 0
        for future in concurrent.futures.as_completed(futures):
            status, fname = future.result()
            if status:
                print(f"成功处理: {fname}")
                success_count += 1

    total_time = time.time() - total_start
    print(f"\n处理完成: {success_count}/{len(common_files)} 成功")
    print(f"总耗时: {total_time:.2f}秒")
    print(f"输出目录: {os.path.abspath(OUTPUT_DIR)}")