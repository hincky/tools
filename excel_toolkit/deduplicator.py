import pandas as pd
import os
from datetime import datetime
import configparser
import string
import argparse

class ExcelDeduplicator:
    def __init__(self, config_path='config.ini'):
        self.config = self.load_config(config_path)
        self.start_column = self.config['columns']['start_column'].strip()
        self.end_column = self.config['columns']['end_column'].strip()
        # 读取必填列配置
        self.required_columns = [
            col.strip().upper() 
            for col in self.config['columns']['required_columns'].split(',')
            if col.strip()
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
    
    def is_empty_value(self, value):
        """检查值是否为空"""
        if pd.isna(value):  # 检查 NaN
            return True
        if isinstance(value, str):
            # 处理空字符串和只包含空白字符的情况
            return value.strip() == ''
        return False
    
    def deduplicate_excel(self, input_file, output_dir=None):
        try:
            print(f"正在读取文件: {input_file}")
            df = pd.read_excel(input_file, header=None)
            
            print("\n文件中的列数:", len(df.columns))
            rows_before = len(df)
            
            # 1. 检查必填列（在任何其他处理之前）
            for col in self.required_columns:
                col_idx = self.get_column_index(col)
                if col_idx >= len(df.columns):
                    raise ValueError(f"必填列 {col} 超出文件实际列数")
                    
                # 使用严格的空值检查
                is_empty = df[col_idx].apply(self.is_empty_value)
                df = df[~is_empty]
                print(f"检查必填列 {col}: 删除了 {rows_before - len(df)} 行空值")
                rows_before = len(df)
            
            # 2. 处理指定列范围
            start_idx = self.get_column_index(self.start_column)
            end_idx = self.get_column_index(self.end_column)
            
            if start_idx > end_idx:
                raise ValueError("起始列不能大于结束列")
                
            if end_idx >= len(df.columns):
                raise ValueError(f"列范围超出文件实际列数 (文件共有 {len(df.columns)} 列)")
            
            # 只保留指定范围的列
            df = df.iloc[:, start_idx:end_idx + 1]
            
            print(f"\n已选择列范围: {self.start_column} - {self.end_column}")
            print(f"保留的列数: {len(df.columns)}")
            
            # 3. 删除所有列都为空的行
            df = df.dropna(how='all')
            
            # 4. 去重
            df_deduplicated = df.drop_duplicates()
            
            rows_after = len(df_deduplicated)
            
            if output_dir is None:
                output_dir = os.path.dirname(input_file) or '.'
            
            filename = os.path.basename(input_file)
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(output_dir, f"{name}_cleaned_{timestamp}{ext}")
            
            df_deduplicated.to_excel(output_file, index=False, header=False)
            
            print(f"\n处理完成！")
            print(f"处理列范围: {self.start_column} - {self.end_column}")
            print(f"必填列: {', '.join(self.required_columns)}")
            print(f"原始行数: {rows_before}")
            print(f"处理后行数: {rows_after}")
            print(f"删除的行数: {rows_before - rows_after}")
            print(f"处理后的文件已保存至: {output_file}")
            
        except Exception as e:
            print(f"处理出错: {str(e)}")
            import traceback
            print("\n详细错误信息:")
            print(traceback.format_exc())

def main():
    parser = argparse.ArgumentParser(description='Excel文件处理工具')
    parser.add_argument('input_file', help='输入的Excel文件路径')
    parser.add_argument('--output-dir', help='输出目录（可选）')
    parser.add_argument('--config', default='config.ini', help='配置文件路径（可选）')
    
    args = parser.parse_args()
    
    deduplicator = ExcelDeduplicator(args.config)
    deduplicator.deduplicate_excel(args.input_file, args.output_dir)

if __name__ == "__main__":
    main()
