import os
import cv2
import numpy as np
from typing import Dict, List


def calculate_entropy(image: np.ndarray) -> float:
    """计算灰度图像的信息熵"""
    hist = np.histogram(image.flatten(), bins=256, range=[0, 256])[0]
    hist = hist / hist.sum()  # 归一化为概率分布
    hist = hist[hist > 0]  # 避免log2(0)导致的错误
    return -np.sum(hist * np.log2(hist))


def calculate_avg_gradient(image: np.ndarray) -> float:
    """计算灰度图像的平均梯度"""
    gx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    gy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    gradient = np.sqrt(gx ** 2 + gy ** 2)
    return np.mean(gradient)


def batch_process(folder_path: str) -> Dict[str, List[float]]:
    """批量处理文件夹中的红外图像"""
    results = {"entropy": [], "gradient": []}
    valid_exts = (".jpg", ".jpeg", ".png", ".bmp")

    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(valid_exts):
            continue

        filepath = os.path.join(folder_path, filename)
        try:
            # 读取灰度图并校验数据
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            if img is None:
                raise ValueError(f"无法读取图像: {filename}")

            # 计算指标
            entropy = calculate_entropy(img)
            avg_grad = calculate_avg_gradient(img)

            # 保存结果
            results["entropy"].append(entropy)
            results["gradient"].append(avg_grad)
            print(f"{filename}: 信息熵={entropy:.2f} bits, 平均梯度={avg_grad:.2f}")

        except Exception as e:
            print(f"处理 {filename} 时出错: {str(e)}")

    return results


def analyze_results(results: Dict[str, List[float]]) -> None:
    """分析统计结果"""
    if not results["entropy"]:
        print("未找到有效图像")
        return

    # 计算极值和均值
    max_entropy = max(results["entropy"])
    max_gradient = max(results["gradient"])
    avg_entropy = np.mean(results["entropy"])
    avg_gradient = np.mean(results["gradient"])

    # 输出统计报告
    print("\n===== 统计分析 =====")
    print(f"最高信息熵: {max_entropy:.2f} bits")
    print(f"最高平均梯度: {max_gradient:.2f}")
    print(f"信息熵平均值: {avg_entropy:.2f} bits")
    print(f"平均梯度均值: {avg_gradient:.2f}")


if __name__ == "__main__":
    folder = "main"  # 替换为实际文件夹路径
    results = batch_process(folder)
    analyze_results(results)