# -*- coding: utf-8 -*-

"""
Step01_Titanic_EDA.py
타이타닉 생존자 데이터 탐색 (Exploratory Data Analysis)
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 로드 (Seaborn 내장 데이터셋 활용)
print("=== 1. Loading Data ===")
df = sns.load_dataset('titanic')
print(f"Shape: {df.shape}")
print(df.head())


print("\n=== 2. Basic Info & Missing Values ===")
df.info()
print(f"\nMissing Values:\n{df.isnull().sum()}")


print("\n=== 3. Statistical Summary ===")
print(df.describe())
print("\n--- Object Columns ---")
print(df.describe(include=['object', 'category']))


print("\n=== 4. Visualization (Survival Rate) ===")
# 한글 폰트 설정이 안 되어 있을 수 있으므로 영문으로 표기
# 생존자 수 (Countplot)
plt.figure(figsize=(6, 4))
sns.countplot(x='survived', data=df)
plt.title('Survival Count (0=Die, 1=Survive)')
plt.show()

# 성별에 따른 생존율 (Barplot)
plt.figure(figsize=(6, 4))
sns.barplot(x='sex', y='survived', data=df)
plt.title('Survival Rate by Sex')
plt.show()

# 객실 등급별 생존율
plt.figure(figsize=(6, 4))
sns.barplot(x='pclass', y='survived', hue='sex', data=df)
plt.title('Survival Rate by Pclass & Sex')
plt.show()
