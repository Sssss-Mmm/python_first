import pandas as pd
print(pd.__version__)

data = [1,2,3,4]
index = ["A","B","C","D"]
series1 = pd.Series(data=data, index=index)
print(series1)
data = {"column1":[1,2,3,4], "column2" : ["a","b","c","d"]}
dataFrame1 = pd.DataFrame(data, index=index)
print(dataFrame1)

data = [[1, "a"],[2, "b"], [3, "c"], [4, "d"]]
columns = ["col1", "col2"]
dataFrame2 = pd.DataFrame(data, columns=columns)
print(dataFrame2)

# dataFrame3 = pd.DataFrame(data, columns=columns, index=index)
dataFrame3 = pd.DataFrame(data, index, columns)
print(dataFrame3)
