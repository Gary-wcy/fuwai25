import os
import cv2
import numpy as np
from skimage import exposure, feature
from tqdm import tqdm
from scipy import stats
from scipy.fftpack import dct
import pandas as pd


def calculate_dynamic_range(img):
    """计算16位红外图像动态范围（分贝）"""
    max_val = img.max()
    min_val = img[img > 0].min() if np.any(img > 0) else 1e-6  # 避免除以0
    return 20 * np.log10(max_val / min_val)


def estimate_noise_level(img):
    """基于DCT变换的噪声水平估计"""
    dct_coeffs = dct(dct(img, axis=0, norm='ortho'), axis=1, norm='ortho')
    abs_dct = np.abs(dct_coeffs)
    robust_std = stats.median_abs_deviation(abs_dct.flatten(), scale='normal')
    return robust_std


def calculate_edge_strength(img):
    """使用Scharr算子计算边缘强度"""
    grad_x = cv2.Scharr(img, cv2.CV_64F, 1, 0)
    grad_y = cv2.Scharr(img, cv2.CV_64F, 0, 1)
    return np.sqrt(grad_x**2 + grad_y**2).mean()


def calculate_contrast(img):
    """计算图像对比度"""
    return img.std() / (img.mean() + 1e-6)  # 避免除以0


def calculate_brightness(img):
    """计算图像亮度"""
    return img.mean()


def process_images(folder_a, folder_b):
    """处理去烟前和去烟后的图像，计算各项指标"""
    metrics = []

    # 获取匹配的文件列表
    files = sorted(f for f in os.listdir(folder_a) if f.lower().endswith(('.png', '.jpg', '.tiff')))

    for filename in tqdm(files, desc="Processing Images"):
        # 读取并预处理图像
        img_a = cv2.imread(os.path.join(folder_a, filename), cv2.IMREAD_ANYDEPTH)
        img_b = cv2.imread(os.path.join(folder_b, filename), cv2.IMREAD_ANYDEPTH)

        if img_a is None or img_b is None:
            print(f"Warning: {filename} skipped (invalid image)")
            continue

        # 调整A图像尺寸
        img_a = cv2.resize(img_a, (640, 360), interpolation=cv2.INTER_AREA)

        if img_a.shape != img_b.shape:
            print(f"Shape mismatch after resize: {filename}")
            continue

        # 转换为8bit计算质量指标
        img_a_8bit = exposure.rescale_intensity(img_a, out_range=(0, 255)).astype('uint8')
        img_b_8bit = exposure.rescale_intensity(img_b, out_range=(0, 255)).astype('uint8')

        # 计算各项指标
        metrics.append({
            'filename': filename,
            'pre_Noise': estimate_noise_level(img_a),
            'post_Noise': estimate_noise_level(img_b),
            'pre_DynamicRange': calculate_dynamic_range(img_a),
            'post_DynamicRange': calculate_dynamic_range(img_b),
            'pre_Variance': img_a.var(),
            'post_Variance': img_b.var(),
            'pre_EdgeStrength': calculate_edge_strength(img_a),
            'post_EdgeStrength': calculate_edge_strength(img_b),
            'pre_Contrast': calculate_contrast(img_a),
            'post_Contrast': calculate_contrast(img_b),
            'pre_Brightness': calculate_brightness(img_a),
            'post_Brightness': calculate_brightness(img_b)
        })

    return pd.DataFrame(metrics)


def analyze_results(df):
    """分析结果，计算平均值和最优值"""
    analysis = {}

    # 各指标最优方向
    optimal_direction = {
        'Noise': 'lower',
        'DynamicRange': 'higher',
        'Variance': 'higher',
        'EdgeStrength': 'higher',
        'Contrast': 'higher',
        'Brightness': 'higher'
    }

    # 统计平均和最优值
    for metric in ['Noise', 'DynamicRange', 'Variance', 'EdgeStrength', 'Contrast', 'Brightness']:
        pre_vals = df[f'pre_{metric}']
        post_vals = df[f'post_{metric}']

        # 平均值变化
        analysis[f'avg_{metric}'] = {
            'pre': pre_vals.mean(),
            'post': post_vals.mean(),
            'delta': post_vals.mean() - pre_vals.mean()
        }

        # 最优值判断
        if optimal_direction[metric] == 'lower':
            analysis[f'best_{metric}'] = {
                'pre': pre_vals.min(),
                'post': post_vals.min(),
                'improvement': post_vals.min() < pre_vals.min()
            }
        else:
            analysis[f'best_{metric}'] = {
                'pre': pre_vals.max(),
                'post': post_vals.max(),
                'improvement': post_vals.max() > pre_vals.max()
            }

    return analysis


if __name__ == "__main__":
    # 输入路径设置
    folder_a = "images-hw"  # 去烟前图像
    folder_b = "main" # 去烟后图像

    # 处理图像并保存结果
    df = process_images(folder_a, folder_b)
    df.to_csv("image_metrics.csv", index=False)

    # 生成统计报告
    analysis = analyze_results(df)
    report = pd.DataFrame({
        'Metric': ['NoiseLevel', 'DynamicRange', 'Variance', 'EdgeStrength', 'Contrast', 'Brightness'],
        'Average_Pre': [analysis[f'avg_{m}']['pre'] for m in
                        ['Noise', 'DynamicRange', 'Variance', 'EdgeStrength', 'Contrast', 'Brightness']],
        'Average_Post': [analysis[f'avg_{m}']['post'] for m in
                         ['Noise', 'DynamicRange', 'Variance', 'EdgeStrength', 'Contrast', 'Brightness']],
        'Best_Pre': [analysis[f'best_{m}']['pre'] for m in
                     ['Noise', 'DynamicRange', 'Variance', 'EdgeStrength', 'Contrast', 'Brightness']],
        'Best_Post': [analysis[f'best_{m}']['post'] for m in
                      ['Noise', 'DynamicRange', 'Variance', 'EdgeStrength', 'Contrast', 'Brightness']]
    })

    print("\n统计分析结果：")
    print(report)
    report.to_csv("statistical_report.csv", index=False)