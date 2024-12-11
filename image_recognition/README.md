# 订单图像识别系统

基于 PaddleOCR 的订单图像识别系统，支持自动识别和提取订单信息。

## 功能特点

- 支持多种图片格式（PNG、JPG、JPEG、BMP、GIF）
- 自动识别订单号、客户信息、日期等信息
- 图形用户界面，操作简单
- 支持批量处理（开发中）
- 支持导出为多种格式（开发中）

## 环境要求

- Python 3.8+
- CUDA (可选，用于GPU加速)

## 安装说明

1. 克隆仓库：
```bash
git clone https://github.com/[你的用户名]/image_recognition.git
cd image_recognition
```

2. 创建并激活conda环境：
```bash
conda create -n ocr python=3.8
conda activate ocr
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 激活环境：
```bash
conda activate ocr
```

2. 运行程序：
```bash
python main.py
```

3. 使用界面：
   - 点击"选择图片"按钮选择要识别的图片
   - 点击"开始识别"按钮进行识别
   - 查看识别结果

## 项目结构

```
image_recognition/
├── src/               # 源代码目录
├── models/            # 模型目录
├── docs/              # 文档目录
├── main.py           # 主程序
├── requirements.txt  # 依赖文件
└── README.md        # 项目说明
```

## 贡献指南

1. Fork 本仓库
2. 创建新的分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 联系方式

[你的名字] - [你的邮箱]

项目链接: https://github.com/[你的用户名]/image_recognition