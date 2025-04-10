import argparse
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


def adjust_exposure(img, target_brightness=113, tolerance=5):
    """自动曝光调整函数（适配RGB图像）"""
    start_time = time.time()

    # 转换到灰度图（输入为RGB格式）
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    current_brightness = np.mean(gray)

    if abs(current_brightness - target_brightness) <= tolerance:
        print(f"亮度正常 ({current_brightness:.1f})，不需调整")
        return img

    # 计算调整参数
    if current_brightness < target_brightness - tolerance:
        alpha = min(2.0, target_brightness / max(1, current_brightness))
        beta = min(30, target_brightness - current_brightness) / 2
        print(f"过暗 ({current_brightness:.1f})，增益 α={alpha:.2f}, β={beta:.1f}")
    else:
        alpha = max(0.5, target_brightness / max(1, current_brightness))
        beta = max(-30, target_brightness - current_brightness) / 2
        print(f"过亮 ({current_brightness:.1f})，增益 α={alpha:.2f}, β={beta:.1f}")

    # 应用调整
    adjusted = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)

    print(f"曝光调整耗时: {time.time() - start_time:.4f}s")
    return adjusted


def estimate_smoke_density(gray_image):
    """优化烟雾浓度估计"""
    small_img = cv2.resize(gray_image, (256, 256), interpolation=cv2.INTER_AREA)
    smoothed = cv2.GaussianBlur(small_img, (3, 3), 0)

    grad_x = cv2.Scharr(smoothed, cv2.CV_64F, 1, 0)
    grad_y = cv2.Scharr(smoothed, cv2.CV_64F, 0, 1)
    gradient_magnitude = cv2.magnitude(grad_x, grad_y)

    if np.max(gradient_magnitude) > 0:
        gradient_magnitude /= np.max(gradient_magnitude)

    mean_gradient = np.mean(gradient_magnitude)
    smoke_density = (1.0 - mean_gradient) * 0.4 + 0.1
    return np.clip(smoke_density, 0.1, 0.6)


def enhance_infrared_image(image_path, output_path, save_steps=False):
    """增强红外图像并添加自动曝光控制"""
    process_start = time.time()

    # 读取图像
    ir_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if ir_image is None:
        raise ValueError(f"无法读取图像: {image_path}")

    # 初始处理
    ir_image = cv2.resize(cv2.cvtColor(ir_image, cv2.COLOR_BGR2RGB), (960, 540))
    if save_steps:
        plt.imsave(f"{os.path.splitext(output_path)[0]}_1_original.png", ir_image)

    # 灰度处理
    gray = cv2.cvtColor(ir_image, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    # 降噪
    denoised = cv2.fastNlMeansDenoising(enhanced, None, h=7, templateWindowSize=5, searchWindowSize=5)

    # 直方图拉伸
    small_img = cv2.resize(denoised, (256, 256))
    p_low, p_high = np.percentile(small_img, [2, 98])
    stretched = np.clip((denoised.astype(np.float32) - p_low) * 255.0 / (p_high - p_low), 0, 255)

    # 伽马校正
    gamma = 0.7 - 0.05 * estimate_smoke_density(stretched.astype(np.uint8))
    gamma_corrected = np.power(stretched / 255.0, gamma) * 255.0

    # LAB增强
    lab = cv2.cvtColor(gamma_corrected.astype(np.uint8), cv2.COLOR_GRAY2RGB)
    lab = cv2.cvtColor(lab, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.createCLAHE(clipLimit=1.0).apply(l)
    enhanced_lab = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2RGB)

    # 自动曝光调整
    final_image = adjust_exposure(enhanced_lab)

    # 保存结果
    plt.imsave(output_path, final_image)
    process_time = time.time() - process_start
    print(f'总处理耗时: {process_time:.2f}秒')
    return final_image, process_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='红外图像增强批量处理')
    parser.add_argument('--input_dir', required=True, help='输入文件夹路径')
    parser.add_argument('--output_dir', required=True, help='输出文件夹路径')
    parser.add_argument('--save_steps', action='store_true', help='保存处理中间步骤')

    args = parser.parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    # 支持的文件格式
    valid_exts = ('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')
    file_list = [f for f in os.listdir(args.input_dir) if f.lower().endswith(valid_exts)]

    total_time = 0.0
    processed = 0

    for filename in file_list:
        input_path = os.path.join(args.input_dir, filename)
        output_path = os.path.join(args.output_dir, filename)


        try:
            print(f'\n处理中: {filename}')
            _, duration = enhance_infrared_image(input_path, output_path, args.save_steps)
            total_time += duration
            processed += 1
        except Exception as e:
            print(f'处理 {filename} 失败: {str(e)}')

    # 输出统计信息
    if processed > 0:
        print(f"\n{'=' * 40}")
        print(f"处理完成: 成功 {processed}/{len(file_list)}")
        print(f"总耗时: {total_time:.2f}秒 | 平均: {total_time / processed:.2f}秒/张")
        print(f"输出目录: {os.path.abspath(args.output_dir)}")
        print('=' * 40)
    else:
        print("未找到可处理的图像文件")