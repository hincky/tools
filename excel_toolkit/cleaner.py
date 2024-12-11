import pandas as pd
import os
from datetime import datetime
import configparser
import argparse

class ExcelCleaner:
    def __init__(self, config_path='config.ini'):
        self.config = self.load_config(config_path)
        # 读取要清洗的列
        self.clean_columns = [
            col.strip().upper() 
            for col in self.config['columns']['clean_columns'].split(',')
            if col.strip()
        ]
        # 读取过滤关键词
        self.filter_keywords = [
            keyword.strip() 
            for keyword in self.config['filter']['keywords'].split(',')
            if keyword.strip()
        ]
        
    def load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
            
        config = configparser.ConfigParser()
        config.read(config_path)
        return config
    
    def get_column_index(self, column_letter):
        """将列字母转换为索引"""
        if not column_letter or len(column_letter) != 1:
            raise ValueError(f"无效的列名: {column_letter}")
        return ord(column_letter.upper()) - ord('A')
    
    def contains_keywords(self, value):
        """检查是否包含关键词"""
        if isinstance(value, str):
            return any(keyword in value for keyword in self.filter_keywords)
        return False
    
    def clean_excel(self, input_file, output_dir=None):
        try:
            print(f"正在读取文件: {input_file}")
            df = pd.read_excel(input_file, header=None)
            
            print("\n文件中的列数:", len(df.columns))
            rows_before = len(df)
            
            # 根据关键词过滤行
            rows_before_filter = len(df)
            for col in self.clean_columns:
                col_idx = self.get_column_index(col)
                if col_idx >= len(df.columns):
                    print(f"警告: 列 {col} 超出文件范围，已跳过")
                    continue
                    
                # 找出不包含关键词的行
                mask = ~df[col_idx].apply(self.contains_keywords)
                df = df[mask]
                print(f"清洗列 {col}: 删除了 {rows_before_filter - len(df)} 行包含关键词的数据")
                rows_before_filter = len(df)
            
            rows_after = len(df)
            
            # 生成输出文件
            if output_dir is None:
                output_dir = os.path.dirname(input_file) or '.'
            
            filename = os.path.basename(input_file)
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(output_dir, f"{name}_cleaned_{timestamp}{ext}")
            
            df.to_excel(output_file, index=False, header=False)
            
            print(f"\n清洗完成！")
            print(f"清洗的列: {', '.join(self.clean_columns)}")
            print(f"过滤的关键词: {', '.join(self.filter_keywords)}")
            print(f"原始行数: {rows_before}")
            print(f"处理后行数: {rows_after}")
            print(f"删除的行数: {rows_before - rows_after}")
            print(f"清洗后的文件已保存至: {output_file}")
            
        except Exception as e:
            print(f"处理出错: {str(e)}")
            import traceback
            print("\n详细错误信息:")
            print(traceback.format_exc())

def main():
    parser = argparse.ArgumentParser(description='Excel数据清洗工具')
    parser.add_argument('input_file', help='输入的Excel文件路径')
    parser.add_argument('--output-dir', help='输出目录（可选）')
    parser.add_argument('--config', default='config.ini', help='配置文件路径（可选）')
    
    args = parser.parse_args()
    
    cleaner = ExcelCleaner(args.config)
    cleaner.clean_excel(args.input_file, args.output_dir)

if __name__ == "__main__":
    main() 