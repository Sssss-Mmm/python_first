# -*- coding: utf-8 -*-

"""
Step02_Files_IO_Basic.py
파일 입출력 (File I/O: CSV, Excel)
"""
import pandas as pd
import os

# 예제용 데이터 생성
data = {
    "Name": ["Kim", "Lee", "Park", "Choi"],
    "Score": [85, 90, 78, 92],
    "Grade": ["B", "A", "C", "A"]
}
df = pd.DataFrame(data)
print(f"Original DataFrame:\n{df}")

# 파일 경로 설정 (현재 디렉토리)
base_dir = "data_samples"
os.makedirs(base_dir, exist_ok=True)
csv_path = os.path.join(base_dir, "scores.csv")
json_path = os.path.join(base_dir, "scores.json")

print("\n=== 1. Writing to CSV ===")
# index=False: 인덱스(0,1,2..)는 저장하지 않음
df.to_csv(csv_path, index=False, encoding='utf-8-sig') 
print(f"Saved to {csv_path}")


print("\n=== 2. Reading from CSV ===")
df_loaded = pd.read_csv(csv_path)
print(f"Loaded from CSV:\n{df_loaded}")


print("\n=== 3. JSON I/O ===")
df.to_json(json_path, orient='records', indent=4, force_ascii=False)
print(f"Saved to {json_path}")

df_json = pd.read_json(json_path)
print(f"Loaded from JSON:\n{df_json}")

# Excel은 openpyxl 등 추가 라이브러리가 필요할 수 있어 코드는 포함하되 실행 시 주의
# pip install openpyxl
# df.to_excel("scores.xlsx", index=False)
# df_excel = pd.read_excel("scores.xlsx")
