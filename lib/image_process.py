import cv2
import numpy as np

def preprocess_image_for_ocr(image_path):
    # 读取图像
    image = cv2.imread(image_path)

    # 转换为灰度图像
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 应用高斯模糊
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # 边缘检测
    edged_image = cv2.Canny(blurred_image, 50, 150)

    # 进行二值化
    _, binary_image = cv2.threshold(edged_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return binary_image

# 示例用法
if __name__ == "__main__":
    processed_image = preprocess_image_for_ocr('/Users/qiaoyinbo/Downloads/A.jpg')
    cv2.imshow('Processed Image', processed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()