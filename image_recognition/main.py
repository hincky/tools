import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
from src.image_processor import ImageProcessor

class ImageRecognitionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("图像识别系统")
        self.window.geometry("800x600")
        
        self.processor = ImageProcessor()
        self.setup_ui()
        
    def setup_ui(self):
        # 创建左侧面板
        left_panel = tk.Frame(self.window)
        left_panel.pack(side=tk.LEFT, padx=10, pady=10)
        
        # 创建右侧面板
        right_panel = tk.Frame(self.window)
        right_panel.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # 图片显示区域
        self.image_label = tk.Label(left_panel)
        self.image_label.pack(pady=10)
        
        # 按钮区域
        btn_frame = tk.Frame(right_panel)
        btn_frame.pack(pady=10)
        
        # 选择图片按钮
        self.select_btn = tk.Button(
            btn_frame,
            text="选择图片",
            command=self.select_image
        )
        self.select_btn.pack(pady=5)
        
        # 识别按钮
        self.recognize_btn = tk.Button(
            btn_frame,
            text="开始识别",
            command=self.recognize_image,
            state=tk.DISABLED
        )
        self.recognize_btn.pack(pady=5)
        
        # 结果显示区域
        self.result_text = tk.Text(right_panel, height=10, width=40)
        self.result_text.pack(pady=10)
        
    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[
                ("图片文件", "*.png *.jpg *.jpeg *.bmp *.gif")
            ]
        )
        if file_path:
            self.current_image_path = file_path
            self.display_image(file_path)
            self.recognize_btn.config(state=tk.NORMAL)
            
    def display_image(self, image_path):
        # 读取并显示图片
        image = Image.open(image_path)
        # 调整图片大小以适应显示区域
        image = image.resize((400, 400), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
    def recognize_image(self):
        try:
            # 识别订单
            result = self.processor.process_image(self.current_image_path)
            
            # 显示结果
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "识别结果：\n")
            self.result_text.insert(tk.END, result)
            
            # 可以添加导出功能按钮
            self.export_btn.config(state=tk.NORMAL)
        except Exception as e:
            messagebox.showerror("错误", f"识别失败：{str(e)}")
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ImageRecognitionApp()
    app.run() 