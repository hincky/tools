import cv2
import numpy as np

def resize_image(image, target_size):
    """调整图像大小"""
    return cv2.resize(image, target_size)

def normalize_image(image):
    """归一化图像"""
    return image / 255.0

def load_image(image_path):
    """加载图像"""
    image = cv2.imread(image_path)
    if image is None:
        raise Exception("无法加载图像")
    return image 