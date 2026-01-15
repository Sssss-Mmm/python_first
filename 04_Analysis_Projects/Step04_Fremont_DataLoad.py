# -*- coding: utf-8 -*-

"""
Step04_Fremont_DataLoad.py
프리몬트 교량 자전거 통행량 데이터 로드 (Data Load & Cleaning)
"""
import pandas as pd
import os
import matplotlib.pyplot as plt

# 데이터 다운로드 URL
URL = "https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD"
FILENAME = "FremontBridge.csv"

def get_fremont_data(filename=FILENAME, force_download=False):
    if force_download or not os.path.exists(filename):
        print("Downloading dataset...")
        try:
            from urllib.request import urlretrieve
            urlretrieve(URL, filename)
            print("Download complete.")
        except Exception as e:
            print(f"Failed to download: {e}")
            return None
    
    # parse_dates: 날짜 컬럼을 datetime으로 변환
    # index_col: 날짜를 인덱스로 설정
    df = pd.read_csv(filename, index_col='Date', parse_dates=True)
    
    # 컬럼명 단축
    df.columns = ["West", "East"]
    df["Total"] = df["West"] + df["East"]
    return df

print("=== 1. Load Data ===")
df = get_fremont_data()

if df is not None:
    print(df.head())
    print(f"\nShape: {df.shape}")
    
    print("\n=== 2. Basic Plot ===")
    # 주간 데이터 합계 시각화
    df.resample('W').sum().plot(figsize=(10, 6))
    plt.ylabel('Weekly bicycle count')
    plt.title('Fremont Bridge Bicycle Counts (Weekly)')
    plt.show()
    
    # 전처리된 데이터 저장 (Pickle로 저장하여 타입 정보 유지)
    df.to_pickle("fremont_clean.pkl")
    print("\n>> Saved to 'fremont_clean.pkl'")
