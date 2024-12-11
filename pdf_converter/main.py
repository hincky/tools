from pdf2docx import Converter
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import tkinter.ttk as ttk  # 导入ttk模块以使用进度条

class PDFConverter:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("PDF转Word转换器")
        self.window.geometry("400x200")
        
        # 创建界面元素
        self.setup_ui()
        
    def setup_ui(self):
        # 选择文件按钮
        self.select_btn = tk.Button(
            self.window, 
            text="选择PDF文件", 
            command=self.select_file
        )
        self.select_btn.pack(pady=20)
        
        # 显示选中的文件路径
        self.file_label = tk.Label(self.window, text="未选择文件")
        self.file_label.pack(pady=10)
        
        # 转换按钮
        self.convert_btn = tk.Button(
            self.window, 
            text="开始转换", 
            command=self.convert_pdf,
            state=tk.DISABLED
        )
        self.convert_btn.pack(pady=20)
        
        # 初始化进度条
        self.progress = ttk.Progressbar(self.window, orient='horizontal', length=300, mode='determinate')
        self.progress.pack(pady=10)
        
    def select_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF文件", "*.pdf")]
        )
        if file_path:
            self.file_path = file_path
            self.file_label.config(text=os.path.basename(file_path))
            self.convert_btn.config(state=tk.NORMAL)
    
    def convert_pdf(self):
        try:
            # 生成不覆盖原文件的输出文件路径
            output_file = os.path.splitext(self.file_path)[0] + '_converted.docx'
            
            # 创建转换器实例
            cv = Converter(self.file_path)
            
            # 设置进度条最大值
            self.progress['maximum'] = 100
            
            # 执行转换并更新进度条
            cv.convert(output_file, start=0, end=None, progress_callback=self.update_progress)
            cv.close()
            
            messagebox.showinfo("成功", "转换完成！")
        except Exception as e:
            messagebox.showerror("错误", f"转换失败：{str(e)}")
    
    def update_progress(self, progress):
        # 更新进度条的值
        self.progress['value'] = progress * 100
        self.window.update_idletasks()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PDFConverter()
    app.run() 