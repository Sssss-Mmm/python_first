"""
Pandas Data Manipulation Example
--------------------------------
이 파일은 Pandas의 데이터 변형 및 결합 기능을 다룹니다.
1. Merge/Concat: SQL Join과 유사하게 두 데이터프레임을 합치는 방법.
2. Apply/Map: 사용자 정의 함수를 데이터프레임의 행/열에 적용.
3. Missing Data Handling: 결측치(NaN)를 찾고 처리(채우기/삭제)하는 방법.
"""

import pandas as pd
import numpy as np

def run_pandas_manipulation_examples():
    print("=== 1. Merge & Concat Example ===")
    # 고객 데이터
    df_customers = pd.DataFrame({
        'customer_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Charlie', 'David']
    })
    
    # 주문 데이터
    df_orders = pd.DataFrame({
        'order_id': [101, 102, 103, 104, 105],
        'customer_id': [1, 2, 2, 5, 1], # 5번 고객은 목록에 없음
        'amount': [250, 100, 150, 300, 200]
    })
    
    print("Customers:\n", df_customers)
    print("Orders:\n", df_orders)
    
    # Inner Join: 두 테이블에 모두 존재하는 키만 결합
    merged_inner = pd.merge(df_customers, df_orders, on='customer_id', how='inner')
    print("\nInner Merge (Common IDs):\n", merged_inner)
    
    # Left Join: 왼쪽(Customers) 기준으로 결합
    merged_left = pd.merge(df_customers, df_orders, on='customer_id', how='left')
    print("\nLeft Merge (All Customers):\n", merged_left) # David는 주문이 없어 NaN 


    print("\n=== 2. Apply & Map Example ===")
    # 데이터 생성
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [10, 20, 30]
    })
    
    # Apply: 각 열(또는 행)에 함수 적용
    # 예: 각 컬럼의 최대값 - 최소값
    stats = df.apply(lambda x: x.max() - x.min())
    print("Column Range (Max-Min):\n", stats)
    
    # Map: Series의 각 요소에 변환 적용 (주로 범주형 데이터 변환에 사용)
    df['Category'] = df['A'].map({1: 'Low', 2: 'Medium', 3: 'High'})
    print("Mapped Category:\n", df)


    print("\n=== 3. Missing Data Handling Example ===")
    df_missing = pd.DataFrame({
        'A': [1, 2, np.nan, 4],
        'B': [5, np.nan, np.nan, 8],
        'C': [10, 11, 12, 13]
    })
    print("Original with Missing:\n", df_missing)
    
    # 결측치 채우기 (0으로)
    df_filled = df_missing.fillna(0)
    print("Filled with 0:\n", df_filled)
    
    # 결측치 채우기 (평균값으로)
    df_filled_mean = df_missing.copy()
    df_filled_mean['A'] = df_filled_mean['A'].fillna(df_filled_mean['A'].mean())
    print("Column A filled with Mean:\n", df_filled_mean)
    
    # 결측치가 있는 행 제거
    df_dropped = df_missing.dropna()
    print("Rows with NaN dropped:\n", df_dropped)

if __name__ == "__main__":
    run_pandas_manipulation_examples()
