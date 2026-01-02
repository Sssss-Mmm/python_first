"""
Model Evaluation & Optimization Example
---------------------------------------
이 파일은 머신러닝 모델의 성능을 평가하고 최적화하는 과정을 다룹니다.
1. Pipeline: 전처리와 모델 학습 과정을 하나의 파이프라인으로 연결.
2. GridSearchCV: 하이퍼파라미터 튜닝을 통해 최적의 모델 설정 찾기.
3. Evaluation Metrics: 정확도 외의 다양한 평가 지표 (Precision, Recall, F1 등).

* 이 예제는 Scikit-learn의 내장 데이터셋(Breast Cancer)을 사용합니다.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

def run_model_optimization():
    print("=== 1. Data Loading & Splitting ===")
    data = load_breast_cancer()
    X = data.data
    y = data.target
    feature_names = data.feature_names
    
    # 학습/테스트 데이터 분리
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
    

    print("\n=== 2. Pipeline Construction (Scaler + Model) ===")
    # 파이프라인: 스케일링 -> Random Forest 분류기
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('rf', RandomForestClassifier(random_state=42))
    ])
    
    
    print("\n=== 3. Hyperparameter Tuning (GridSearchCV) ===")
    # 탐색할 파이프라인의 파라미터 그리드 정의
    # 'rf__' 접두사를 사용하여 파이프라인 내부 모델의 파라미터 지정
    param_grid = {
        'rf__n_estimators': [50, 100],      # 트리의 개수
        'rf__max_depth': [None, 10, 20],    # 트리의 최대 깊이
        'rf__min_samples_split': [2, 5]     # 노드 분할 최소 샘플 수
    }
    
    # GridSearch 설정 (cv=3: 3-fold 교차 검증)
    grid_search = GridSearchCV(pipeline, param_grid, cv=3, verbose=1, n_jobs=-1)
    
    print("Starting Grid Search... (This might take a moment)")
    grid_search.fit(X_train, y_train)
    
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Best Cross-Validation Score: {grid_search.best_score_:.4f}")
    
    
    print("\n=== 4. Final Evaluation on Test Set ===")
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)
    
    # 평가 리포트
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

if __name__ == "__main__":
    run_model_optimization()
