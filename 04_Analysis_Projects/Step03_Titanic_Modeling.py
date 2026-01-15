# -*- coding: utf-8 -*-

"""
Step03_Titanic_Modeling.py
머신러닝 모델링 (Modeling: Logistic Regression / Random Forest)
"""
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 전처리된 데이터 로드
if not os.path.exists('titanic_processed.csv'):
    print("Error: 'titanic_processed.csv' not found. Run Step02 first.")
    exit()

df = pd.read_csv('titanic_processed.csv')

print("=== 1. Train/Test Split ===")
X = df.drop('survived', axis=1) # Features
y = df['survived']              # Target

# 8:2 비율로 분리
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Train Shape: {X_train.shape}, Test Shape: {X_test.shape}")


print("\n=== 2. Model Training (Logistic Regression) ===")
# 로지스틱 회귀 (분류 모델)
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

print(f"Intercept: {model.intercept_}")
print(f"Coefficients: {model.coef_}")


print("\n=== 3. Evaluation ===")
# 예측
y_pred = model.predict(X_test)

# 정확도
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc:.4f}")

# 혼동 행렬 & 리포트
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))
