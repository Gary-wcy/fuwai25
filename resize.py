import cv2


def resize_image(input_path, output_path):
    """
    最简单的图片resize功能
    参数:
        input_path: 输入图片路径
        output_path: 输出图片路径
    """
    # 读取图片
    img = cv2.imread(input_path)
    if img is None:
        raise ValueError("无法读取图片，请检查路径")

    # 调整尺寸为960x540
    resized_img = cv2.resize(img, (256, 256))

    # 保存结果
    cv2.imwrite(output_path, resized_img)


# 使用示例
input_image = "wuxi_2_2697 (2).jpg"  # 替换为你的输入图片路径
output_image = "resize_wuxi_2_2697(2).jpg"  # 替换为你的输出图片路径

resize_image(input_image, output_image)