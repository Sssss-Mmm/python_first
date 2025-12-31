"""
[20250419_01.py]
타이타닉 생존자 예측 (Classification) 예제입니다.
Scikit-learn의 Decision Tree를 사용하여 승객의 생존 여부를 예측하고 평가합니다.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

def main():
    # 1. 데이터 로드
    # 예제 폴더 내의 train.csv를 사용합니다.
    print("[1] 데이터 로드 중...")
    try:
        df = pd.read_csv('train.csv')
    except FileNotFoundError:
        print("오류: 'train.csv' 파일을 찾을 수 없습니다. 현재 폴더에 파일이 있는지 확인해주세요.")
        return

    print(f"데이터 크기: {df.shape}")
    print(df.head())

    # 2. 데이터 전처리 (Preprocessing)
    print("\n[2] 데이터 전처리 중...")
    
    # 분석에 사용할 Feature 선택
    # Pclass: 티켓 등급, Sex: 성별, Age: 나이, SibSp: 형제/배우자, Parch: 부모/자녀, Fare: 요금
    features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
    target = 'Survived'
    
    X = df[features]
    y = df[target]

    # 결측치 처리 (Missing Values)
    # 나이(Age)가 비어있는 경우 평균값으로 채움
    X = X.copy() # SettingWithCopyWarning 방지
    X['Age'] = X['Age'].fillna(X['Age'].mean())
    
    # 범주형 데이터 변환 (Encoding)
    # 성별(Sex): male -> 0, female -> 1
    X['Sex'] = X['Sex'].map({'male': 0, 'female': 1})
    
    # 전처리 결과 확인
    print("전처리 후 데이터 (상위 5개):")
    print(X.head())

    # 3. 학습/테스트 데이터 분리
    # 전체 데이터를 학습용(80%)과 테스트용(20%)으로 나눕니다.
    print("\n[3] 학습/테스트 데이터 분리 중...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"학습 데이터: {X_train.shape}, 테스트 데이터: {X_test.shape}")

    # 4. 모델 학습 (Decision Tree)
    # 의사결정나무 모델을 사용하여 학습합니다.
    print("\n[4] 모델 학습 중 (Decision Tree)...")
    model = DecisionTreeClassifier(random_state=42, max_depth=5) # 과적합 방지를 위해 깊이 제한
    model.fit(X_train, y_train)
    print("학습 완료!")

    # 5. 모델 평가
    print("\n[5] 모델 평가...")
    y_pred = model.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print(f"정확도 (Accuracy): {acc:.4f}")
    
    print("\n분류 보고서 (Classification Report):")
    print(classification_report(y_test, y_pred))

    # 6. 중요도 시각화
    print("\n[6] 특성 중요도 시각화...")
    importance = model.feature_importances_
    feature_imp = pd.Series(importance, index=features).sort_values(ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_imp, y=feature_imp.index)
    plt.title('Feature Importance (Titanic Survival Prediction)')
    plt.xlabel('Importance Score')
    plt.ylabel('Features')
    
    # 그래프 저장 (화면에 띄우는 대신 파일로 저장)
    plt.tight_layout()
    plt.savefig('titanic_feature_importance.png')
    print("시각화 결과가 'titanic_feature_importance.png'로 저장되었습니다.")
    # plt.show() # 로컬 환경에 따라 주석 해제

if __name__ == "__main__":
    main()
