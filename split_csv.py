#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import csv
import pandas as pd

# 定义输入和输出目录
input_dir = '/Users/zhangzekun/code/anaysis/ll2/csv_output'
output_dir = '/Users/zhangzekun/code/anaysis/ll2/csv_output/split'

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 需要处理的文件列表
files_to_process = [
    '区域档案.csv',
    '区域管理员.csv',
    'CTVT变更记录.csv'
]

# 表名映射，用于从文件内容中提取表名
table_name_mapping = {
    '区域档案.csv': {
        '区域层级表 C_AR_AREA': 'C_AR_AREA',
        '区域层级表 C_AR_AREA_HIS': 'C_AR_AREA_HIS'
    },
    '区域管理员.csv': {
        '区域管理员  C_AR_AREA_MANAGER': 'C_AR_AREA_MANAGER',
        '区域管理员管理清单  C_AR_RESPONSIBLE_AREA': 'C_AR_RESPONSIBLE_AREA'
    },
    'CTVT变更记录.csv': {
        'CTVT变更记录 C_AR_CT_PT_CHANGE_LOG': 'C_AR_CT_PT_CHANGE_LOG',
        'CT 字典表 C_AR_CT': 'C_AR_CT',
        'CT 字典表 C_AR_CT': 'C_AR_PT'  # 注意：原文件中第三个表名也是'CT 字典表 C_AR_CT'，但实际是PT表
    }
}

def process_csv_file(file_path, file_name):
    print(f"处理文件: {file_name}")
    
    # 读取CSV文件内容
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        content = f.readlines()
    
    # 初始化变量
    tables = []
    current_table = []
    in_table = False
    table_name = ""
    
    # 遍历文件的每一行
    for line in content:
        line = line.strip()
        
        # 检查是否是表头行（包含表名）
        found_table_header = False
        for key in table_name_mapping[file_name]:
            if key in line:
                # 如果已经在处理一个表，保存它
                if in_table and current_table:
                    tables.append((table_name, current_table))
                
                # 开始新表
                current_table = [line]
                in_table = True
                table_name = table_name_mapping[file_name][key]
                found_table_header = True
                break
        
        # 如果找到了表头，继续处理下一行
        if found_table_header:
            continue
            
        # 如果是空行且当前正在处理表，则表示当前表结束
        if not line and in_table:
            if current_table:  # 确保表不为空
                tables.append((table_name, current_table))
                current_table = []
                in_table = False
        
        # 如果在处理表中且不是空行，添加到当前表
        elif in_table:
            current_table.append(line)
    
    # 处理最后一个表（如果有）
    if in_table and current_table:
        tables.append((table_name, current_table))
    
    # 保存拆分后的表
    for table_name, table_content in tables:
        output_file = os.path.join(output_dir, f"{table_name}.csv")
        with open(output_file, 'w', encoding='utf-8-sig', newline='') as f:
            for line in table_content:
                f.write(line + '\n')
        print(f"已保存表: {table_name} 到 {output_file}")

# 主函数
def main():
    for file_name in files_to_process:
        file_path = os.path.join(input_dir, file_name)
        if os.path.exists(file_path):
            process_csv_file(file_path, file_name)
        else:
            print(f"文件不存在: {file_path}")

if __name__ == "__main__":
    main()
    print("所有CSV文件拆分完成！")