"""
[20250416_02.py]
Pandas 라이브러리의 핵심 자료구조인 Series와 DataFrame의 생성 및 기초 사용법 예제입니다.
"""
import pandas as pd
print(pd.__version__)
data = [1,2,3,4]
index = ["A","B","C","D"]
series1=pd.Series(data=data,index=index)
print(series1)
data= {"col1":[1,2,3,4],"col2":["a","b","c","d"]}
index=["A","B","C","D"]
dataFrame= pd.DataFrame(data=data,index=index)
print(dataFrame)
data=[[1,"a"],[2,"b"],[3,"c"],[4,"d"]]
columns=["col1","col2"]
dataFrame2=pd.DataFrame(data=data,columns=columns)
print(dataFrame2)
dataFrame3=pd.DataFrame(data=data,index=index,columns=columns)
print(dataFrame3)