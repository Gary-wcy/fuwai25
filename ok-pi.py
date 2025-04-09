import argparse
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time


def estimate_smoke_density(gray_image):
    """优化后的烟雾浓度估计函数"""
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
    smoke_n = 0.5  # 可以视情况调整

    # 只计算处理时间（不包括I/O）
    process_start = time.time()

    # 读取图像不计入处理时间
    ir_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    if ir_image is None:
        raise ValueError(f"无法读取图像: {image_path}")

    ir_image = cv2.resize(cv2.cvtColor(ir_image, cv2.COLOR_BGR2RGB),
                          (960, 540), interpolation=cv2.INTER_AREA)

    if save_steps:
        plt.imsave(f"{os.path.splitext(output_path)[0]}_1_original.png", ir_image)

    gray = cv2.cvtColor(ir_image, cv2.COLOR_RGB2GRAY)

    clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(8, 8))
    enhanced = clahe.apply(gray)

    denoised = cv2.fastNlMeansDenoising(
        enhanced, None, h=7,
        templateWindowSize=5,
        searchWindowSize=5
    )

    small_img = cv2.resize(denoised, (256, 256), interpolation=cv2.INTER_AREA)
    p_low, p_high = np.percentile(small_img, [2, 98])
    stretched = np.clip((denoised.astype(np.float32) - p_low) * 255.0 / (p_high - p_low), 0, 255)

    gamma = 0.7 - 0.05 * smoke_n
    gamma_corrected = np.power(stretched / 255.0, gamma) * 255.0

    lab = cv2.cvtColor(gamma_corrected.astype(np.uint8), cv2.COLOR_GRAY2RGB)
    lab = cv2.cvtColor(lab, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.createCLAHE(clipLimit=1.0).apply(l)
    enhanced_lab = cv2.cvtColor(cv2.merge((l, a, b)), cv2.COLOR_LAB2RGB)

    # 处理结束时间点（保存前）
    process_time = time.time() - process_start

    # 保存图像不计入处理时间
    plt.imsave(output_path, enhanced_lab)

    print(f'处理完成 {os.path.basename(image_path)}，处理耗时: {process_time:.2f}秒')
    return enhanced_lab, process_time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='红外图像增强批量处理')
    parser.add_argument('--input_dir', type=str, required=True, help='输入文件夹路径')
    parser.add_argument('--output_dir', type=str, required=True, help='输出文件夹路径')
    parser.add_argument('--save_steps', action='store_true', help='是否保存中间步骤')

    args = parser.parse_args()

    # 创建输出目录
    os.makedirs(args.output_dir, exist_ok=True)

    # 支持的文件格式
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.tif', '.tiff')

    # 初始化统计变量
    total_process_time = 0.0
    processed_count = 0

    # 遍历输入目录
    for filename in os.listdir(args.input_dir):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(args.input_dir, filename)
            output_path = os.path.join(args.output_dir, filename)

            try:
                print(f'\n正在处理: {filename}')
                _, process_time = enhance_infrared_image(input_path, output_path, args.save_steps)
                total_process_time += process_time
                processed_count += 1
            except Exception as e:
                print(f'处理 {filename} 时发生错误: {str(e)}')

    # 输出统计信息
    if processed_count > 0:
        print(f"\n{'=' * 40}")
        print(f"总处理图片数量: {processed_count}张")
        print(f"总处理时间: {total_process_time:.2f}秒")
        print(f"平均每张处理时间: {total_process_time / processed_count:.2f}秒")
        print(f"处理速度: {processed_count / total_process_time:.2f} FPS")
        print('=' * 40)
    else:
        print("没有找到可处理的图像文件")