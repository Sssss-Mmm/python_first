# -*- coding: utf-8 -*-

"""
Step02_Titanic_Preprocessing.py
데이터 전처리 (Preprocessing: Missing Values & Encoding)
"""
import pandas as pd
import seaborn as sns

# 데이터 로드
df = sns.load_dataset('titanic')

print("=== 1. Handling Missing Values ===")
# 'deck' 열은 결측치가 너무 많아 삭제
df = df.drop(columns=['deck', 'embark_town', 'alive'])

# 'age'는 중앙값으로 채움
df['age'] = df['age'].fillna(df['age'].median())

# 'embarked'는 최빈값으로 채움
mode_emb = df['embarked'].mode()[0]
df['embarked'] = df['embarked'].fillna(mode_emb)

print("Missing Values After Handling:")
print(df.isnull().sum())


print("\n=== 2. Feature Selection & Encoding ===")
# 분석에 필요한 컬럼 선택
# survived: Target
# sex, embarked, pclass: Categorical -> Encoding 필요
# age, sibsp, parch, fare: Numerical
cols = ['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
df = df[cols]

# One-Hot Encoding (get_dummies)
# drop_first=True: 다중공선성 방지 (ex: sex_male만 남기고 sex_female 제거)
df_encoded = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)

print("Encoded DataFrame Head:")
print(df_encoded.head())

# 전처리된 데이터 저장 (CSV)
df_encoded.to_csv('titanic_processed.csv', index=False)
print("\n>> Saved to 'titanic_processed.csv'")
