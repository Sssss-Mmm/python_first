import numpy as np
import pandas as pd
data1 = np.zeros((4,2))
dataFrame1 = pd.DataFrame(data=data1)
print(dataFrame1)

data = [
    ["sun", 10, None],
    ["mon", 7, None],
    ["tue", 200, "어린이날"],
    ["wed", 7, None],
    ["thur", 100, "생일"],
    ["fri", 7, None],
    ["sat", 200, "어버이날"]
]
data1 = [
    [10, 1],
    [7, 2],
    [200, 3],
    [7, 4],
    [100, 5],
    [7, 6],
    [200, 7]
]
index = pd.date_range("20250503", periods=7)
columns = ["일자", "예산", "기념일"]
columns1 = ["예산", "기념일"]
dataFrame2 = pd.DataFrame(data=data, index=index, columns=columns)
dataFrame3 = pd.DataFrame(data=data1, columns=columns1)
print(dataFrame2)

for dformat in dir(pd):
    if dformat.startswith("read_"):
        print(dformat)

df = pd.read_csv("C:/Users/user/Desktop/job/gitRepo/BicycleWeather.csv")
print(df.head(2))
print(df.tail(3))
print(df.sample(5))
df.info()

print(dataFrame2.isna())
print(df.isna().sample(5))
print(df.describe())
# print(df.corr())
df2 = pd.read_csv("C:/Users/user/Desktop/job/gitRepo/FremontBridge.csv")
print(df2.corr())

isnaDataFrame2 = dataFrame2.isna()
print(isnaDataFrame2.groupby("기념일").mean())
print(dataFrame3.groupby("예산").mean())

################  train.csv  ####################

df = pd.read_csv("C:/Users/user/Desktop/job/gitRepo/train.csv")
print(df.sample(5))
df.info()
print(df.describe())

print(df.isna())
# data를 수정해야 함(예를 들면 corr()는 수치형 데이터만 적용가능)
print(df["Survived"])
print(df.Survived)
print(df.head(1)) # index==0인 값
print(df.loc[0, "Name"])
print(df.iloc[0, 3])
sampleDf = df.iloc[0:5, 1:3]
sampleDf = df[["Survived", "Pclass", "Age", "SibSp", "Parch", "Fare"]]
print(sampleDf)
print(sampleDf.corr())
print(sampleDf.groupby("Survived").mean())
mask = (df.Sex == "female")
print(mask)
print([[mask]])
sampleDf["New"] = 0
sampleDf["Family"] \
    = sampleDf["SibSp"] + sampleDf["Parch"]
print(sampleDf)
sampleDf = sampleDf.drop(labels="New", axis=1)
print(sampleDf)
sampleDf.drop(columns=["Family"], inplace=True)
print(sampleDf)
np.random.seed(0)
size = len(sampleDf)
print(size) # count of rows
data = np.random.rand(size) # psudo data created.
print(data)
standard = pd.Series(data, name="standard")
print(standard)
print(pd.concat(objs=[sampleDf, standard], axis=1))

data = np.arange(len(sampleDf.columns)).reshape(1, -1)
print(data)
number = pd.DataFrame(data, columns=sampleDf.columns)
print(number)
rdf = pd.concat([sampleDf, number], axis=0)
print(rdf)
rdf = rdf.reset_index(drop=True)
print(rdf)
df.rename({"Age" : "나이"}, axis=1)
age_mean = sampleDf.Age.mean()
print(age_mean)
sampleDf["Age"] = sampleDf["Age"].fillna(value=age_mean)
print(sampleDf[888:])
def f(x) : 
    return len(str(x))
print(df.applymap(f))
print(f(df))
print("########## map() test ###########")
print(df.Sex)
print(df.Sex.map(lambda x : 0 if x == "female" else 1))
print(df.Sex.map({"female":10, "male" : 20}))

def f2(x, n) :  return x ** n
print(df[["Age", "SibSp", "Fare"]].apply(f2, args=[2]))
df.to_csv("titanic.csv")
df.to_clipboard()

for dformat in dir(df):
    if dformat.startswith("to_"):
        print(dformat)
