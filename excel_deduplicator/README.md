# Excel 去重工具

这是一个用于处理 Excel 文件的工具，可以根据配置的列范围进行数据清洗和去重。

## 功能特点

- 支持指定列范围进行处理
- 支持配置必填列，自动删除必填列为空的行
- 自动删除空行
- 对指定范围内的数据进行去重
- 保留原始文件，生成新的处理后文件

## 安装依赖
```bash
pip install -r requirements.txt
```

## 配置说明

在 `config.ini` 文件中配置处理参数：
```ini
[columns]
# 处理的列范围（使用Excel列字母）
start_column = B
end_column = H
# 必填列（逗号分隔的列字母，这些列不能为空）
required_columns = C
```

## 使用方法
基本用法：
```bash
python main.py input.xlsx
```
指定输出目录
```bash
python main.py input.xlsx --output-dir /path/to/output.xlsx
```
使用自定义配置文件
```bash
python main.py input.xlsx --config custom_config.ini
```

## 处理流程

1. 检查必填列，删除任何必填列为空的行
2. 截取指定列范围的数据
3. 删除全空行
4. 去除重复数据
5. 生成新的处理后文件

## 输出说明

程序会输出详细的处理信息：
- 处理的列范围
- 必填列列表
- 原始行数
- 处理后行数
- 删除的行数
- 输出文件路径

输出文件命名格式：原文件名_cleaned_时间戳.xlsx


## 注意事项

- 列名使用 Excel 的字母表示（A, B, C...）
- 必填列可以在处理列范围之外
- 空值判断包括：
  - 空单元格
  - 空字符串
  - 只包含空格的字符串
- 原始文件不会被修改

## 开发环境

- Python 3.6+
- pandas
- openpyxl

## 许可证

MIT License

## 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启一个 Pull Request