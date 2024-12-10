import pandas as pd
import os
from datetime import datetime
import configparser
import string
import argparse

class ExcelDeduplicator:
    def __init__(self, config_path='config.ini'):
        self.config = self.load_config(config_path)
        self.start_column = self.config['columns']['start_column']
        self.end_column = self.config['columns']['end_column']
        
    def load_config(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"配置文件不存在: {config_path}")
            
        config = configparser.ConfigParser()
        config.read(config_path)
        return config
    
    def deduplicate_excel(self, input_file, output_dir=None):
        try:
            # 读取Excel文件
            print(f"正在读取文件: {input_file}")
            # 读取时不使用第一行作为列名
            df = pd.read_excel(input_file, header=None)
            
            # 打印列信息
            print("\n文件中的列数:", len(df.columns))
            
            # 获取要处理的列范围
            start_idx = ord(self.start_column) - ord('A')
            end_idx = ord(self.end_column) - ord('A')
            
            if start_idx > end_idx:
                raise ValueError("起始列不能大于结束列")
                
            # 检查列是否存在
            if end_idx >= len(df.columns):
                raise ValueError(f"列范围超出文件实际列数 (文件共有 {len(df.columns)} 列)")
            
            # 获取原始行数
            rows_before = len(df)
            
            # 1. 只保留指定范围的列（使用iloc进行切片）
            df = df.iloc[:, start_idx:end_idx + 1]
            
            print(f"\n已选择列范围: {self.start_column} - {self.end_column}")
            print(f"保留的列数: {len(df.columns)}")
            
            # 2. 删除所有列都为空的行
            df = df.dropna(how='all')
            
            # 3. 删除任意列包含空值的行
            df = df.dropna(how='any')
            
            # 4. 去重
            df_deduplicated = df.drop_duplicates()
            
            # 获取最终行数
            rows_after = len(df_deduplicated)
            
            # 生成输出文件名
            if output_dir is None:
                output_dir = os.path.dirname(input_file) or '.'
            
            filename = os.path.basename(input_file)
            name, ext = os.path.splitext(filename)
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = os.path.join(output_dir, f"{name}_cleaned_{timestamp}{ext}")
            
            # 保存处理后的文件
            df_deduplicated.to_excel(output_file, index=False, header=False)
            
            print(f"\n处理完成！")
            print(f"处理列范围: {self.start_column} ({start_idx}) - {self.end_column} ({end_idx})")
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
