import pandas as pd
import os

# 엑셀 파일 경로 설정
file_path = r"D:\AI\myproject\느타리버섯-02.14-16.xls"

base_name = os.path.splitext(os.path.basename(file_path))[0]
csv_file_path = f'{base_name}_1kg_standard.csv'

excel_data = pd.read_excel(file_path, sheet_name=0)

# 불필요한 컬럼들 삭제 (도매시장, 도매법인, 산지, 비고)
columns_to_drop = ['도매시장', '도매법인', '산지', '비고']
excel_data_cleaned = excel_data.drop(columns=columns_to_drop)
excel_data_cleaned['무게'] = excel_data_cleaned['규격(전체)'].str.extract(r'(\d+\.?\d*)').astype(float)

# 경락가를 1kg 기준으로 변환
excel_data_cleaned['경락가'] = (excel_data_cleaned['경락가'] / excel_data_cleaned['무게']).astype(int)

# 규격(전체)을 1kg으로 변환
excel_data_cleaned['규격(전체)'] = '1kg'
excel_data_cleaned = excel_data_cleaned.drop(columns=['무게'])
excel_data_cleaned.to_csv(csv_file_path, index=False, encoding='utf-8-sig')
print("저장 완료:", csv_file_path)
