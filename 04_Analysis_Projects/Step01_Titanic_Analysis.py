"""
[20250417_01.py]
Pandas를 이용한 데이터 로드, 결측치 처리, 그룹화(groupby), 그리고 Titanic 데이터셋을 이용한 전처리 및 분석 예제입니다.
"""
import pandas as pd
import numpy as np
for dformat in dir(pd):
    if dformat.startswith("read_"):
        print(dformat)
data1 = np.zeros((4,2))
dataFrame1 =pd.DataFrame(data=data1)
print(dataFrame1)

data2 = [["Sun",10,None],["Mon",7,None],
         ["Tue",200,"어린이날"],["Wed",7,None],
         ["Thur",100,"생일"],["Fri",7,None],
         ["Sat",200,"어버이날"]]
data3 = [[10,1],[7,2],
         [200,3],[7,4],
         [100,5],[7,6],
         [200,7]]
index = pd.date_range("20200503",periods=7)
columns = ["요일","예산","기념일"]
columns1 = ["예산","기념일"]
dataFrame2 = pd.DataFrame(data=data2,index=index, columns=columns)
dataFrame3 = pd.DataFrame(data=data3, columns=columns1)
print(dataFrame2)
df = pd.read_csv("../data/BicycleWeather.csv") # 날씨 데이터 로드
df2 = pd.read_csv("../data/FremontBridge2.csv") # 프리몬트 교량 데이터 로드
print(df.head(2)) # 상위 2개 행 출력
print(df.tail(3))
print(df.sample(5))
print(df.info()) # 함수의 리턴이 뭔지 확인하기

print("dataFrame2.isna()",dataFrame2.isna())
print(df.isna().sample(5))
print(df.describe())
print(df2.corr())
print(df2.mean())

isnaDataFrame2= dataFrame2.isna() # 결측치 여부 확인 (True/False)
print(isnaDataFrame2.groupby("기념일").mean()) # 기념일별 결측치 비율
print(dataFrame3.groupby("예산").mean()) # 예산별 평균

print("--------------train.csv---------------")
df = pd.read_csv("../data/train.csv")
print(df.sample(5))
df.info()
print(df.isna())
#data를 수정해야됨(예를 들면 corr()는 수치형)
print(df["Survived"])
print(df.Survived)
print(df.head(1))
print(df.loc[0,"Name"])
print(df.iloc[0,3])
sampleDf= df.iloc[0:5,1:3] # iloc을 이용한 인덱싱 (행: 0~4, 열: 1~2)
sampleDf2=df[["Survived","Pclass","Age","SibSp","Parch","Fare"]] # 주요 컬럼 선택
print(sampleDf)
print(sampleDf.corr())
print(sampleDf.groupby("Survived").mean())
print(sampleDf2)
mask = (df.Sex == "female")
print(mask)
print([[mask]])
# print(df.corr())
# print(df.groupby("survived").mean())
sampleDf2["New"]=0 # 새로운 컬럼 추가
sampleDf2["Family"]=sampleDf2["SibSp"]+sampleDf2["Parch"] # 가족 수 파생 변수 생성
sampleDf2= sampleDf2.drop(labels="New",axis=1) # 컬럼 삭제 (방법 1)
sampleDf2.drop(columns=["Family"],inplace=True) # 컬럼 삭제 (방법 2, inplace=True)
print(sampleDf2)
np.random.seed(0)
data=np.random.randn(len(sampleDf2))
print("data",data)
standard=pd.Series(data,name="standard")
print(standard)
print(pd.concat(objs=[sampleDf2,standard],axis=1))

data= np.arange(len(sampleDf2.columns)).reshape(1,-1)
number = pd.DataFrame(data,columns=sampleDf2.columns)
print("number=",number)
rdf= pd.concat([sampleDf2,number],axis=0)
print(rdf)
rdf = rdf.reset_index(drop=True)
print(rdf)
sampleDf2=sampleDf2.rename({"Age":"나이"},axis=1)
print(sampleDf2)
age_mean=sampleDf2.나이.mean() # 나이 평균 계산
print(age_mean)
sampleDf2["나이"]=sampleDf2["나이"].fillna(value=age_mean) # 결측치를 평균값으로 채움
print(sampleDf2[888:])
def f(x):
    """
    입력된 값의 문자열 길이를 반환합니다.
    """
    return len(str(x))
print(f(sampleDf2))
print("-----------------map() test ------------")
print(df.Sex.map(lambda x:0 if x =="female" else 1))
print(df.Sex.map({"female":10,"male":20}))
def f2(x,n):
    """
    x의 n승을 계산하여 반환합니다.
    """
    return x **n
print(df[["Age","SibSp","Fare"]])
print(df[["Age","SibSp","Fare"]].apply(f2,args=[2]))
df.to_csv("titanic.csv")
# df.to_clipboard("123")
for dformat in dir(df):
    if dformat.startswith("to_"):
        print(dformat)