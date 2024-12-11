import cv2
import numpy as np
from paddleocr import PaddleOCR
import json

class ImageProcessor:
    def __init__(self):
        self.initialize_models()
    
    def initialize_models(self):
        """
        初始化OCR模型
        """
        self.ocr = PaddleOCR(use_angle_cls=True, lang='ch', show_log=False)
        
    def process_image(self, image_path):
        """
        处理订单图像
        """
        # 读取图像
        image = cv2.imread(image_path)
        if image is None:
            raise Exception("无法读取图像")
            
        # OCR识别
        result = self.ocr.ocr(image_path, cls=True)
        
        # 解析订单信息
        order_info = self.parse_order_info(result)
        
        return json.dumps(order_info, ensure_ascii=False, indent=2)
    
    def parse_order_info(self, ocr_result):
        """
        解析订单信息
        """
        order_info = {
            "单号": "",
            "打货客户": "",
            "客户电话": "",
            "客户地址": "",
            "打货日期": "",
            "预接货日期": "",
            "商品列表": []
        }
        
        if not ocr_result or not ocr_result[0]:
            return order_info
            
        # 遍历OCR结果
        for line in ocr_result[0]:
            text = line[1][0]
            
            # 提取订单号
            if "No" in text:
                order_info["单号"] = text.split("No")[-1].strip()
                
            # 提取客户信息
            if "客户电话" in text:
                # 查找下一个文本作为电话号码
                next_text = self.find_next_text(ocr_result[0], line)
                if next_text:
                    order_info["客户电话"] = next_text
                    
            # 继续提取其他信息...
            
        return order_info
    
    def find_next_text(self, ocr_result, current_line):
        """
        查找当前行之后的文本
        """
        try:
            current_index = ocr_result.index(current_line)
            if current_index + 1 < len(ocr_result):
                return ocr_result[current_index + 1][1][0]
        except:
            pass
        return "" 