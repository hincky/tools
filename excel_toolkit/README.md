# Excel 工具集

这是一个实用的 Excel 工具集合，提供多种 Excel 文件处理功能。

## 功能列表

### 1. Excel 去重工具

去除 Excel 文件中的重复数据，支持：
- 指定列范围去重
- 必填列检查
- 空值处理

#### 功能特点

- 支持指定列范围进行处理
- 支持配置必填列，自动删除必填列为空的行
- 自动删除空行
- 对指定范围内的数据进行去重
- 保留原始文件，生成新的处理后文件

#### 安装依赖
```bash
pip install -r requirements.txt
```

#### 配置说明

在 `config.ini` 文件中配置处理参数：
```ini
[columns]
# 处理的列范围（使用Excel列字母）
start_column = B
end_column = H
# 必填列（逗号分隔的列字母，这些列不能为空）
required_columns = C
```

#### 使用方法

基本用法：
```bash
python deduplicator.py input.xlsx
```
指定输出目录
```bash
python deduplicator.py input.xlsx --output-dir /path/to/output.xlsx
```
使用自定义配置文件
```bash
python deduplicator.py input.xlsx --config custom_config.ini
```

#### 处理流程

1. 检查必填列，删除任何必填列为空的行
2. 截取指定列范围的数据
3. 删除全空行
4. 去除重复数据
5. 生成新的处理后文件

#### 输出说明

程序会输出详细的处理信息：
- 处理的列范围
- 必填列列表
- 原始行数
- 处理后行数
- 删除的行数
- 输出文件路径

输出文件命名格式：原文件名_cleaned_时间戳.xlsx


#### 注意事项

- 列名使用 Excel 的字母表示（A, B, C...）
- 必填列可以在处理列范围之外
- 空值判断包括：
  - 空单元格
  - 空字符串
  - 只包含空格的字符串
- 原始文件不会被修改

### 2. Excel 合并工具

合并多个 Excel 文件，支持：
- 文件批量合并
- 智能列匹配
- 数据清洗


### 3. Excel 数据清洗工具 (cleaner.py)

根据关键词过滤数据，支持：
- 指定多个清洗列
- 自定义过滤关键词
- 保留原始数据结构

#### 使用方法

```bash
python cleaner.py input.xlsx [选项]
```

选项：
- `--output-dir`: 指定输出目录
- `--config`: 指定配置文件路径

#### 配置说明
在 `config.ini` 中设置：
```ini
[columns]
clean_columns = C, D, E
[filter]
keywords = 软床, 电视柜, 茶几, 床头柜, 床垫, 圆桌, 椅, 售后
```
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