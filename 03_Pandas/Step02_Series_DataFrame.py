"""
[Step 02] Multi-dimensional Array Indexing
------------------------------------------
(참고: Pandas 학습 전 NumPy 차원 이해를 위한 예제입니다.)
3차원 배열을 생성하고 reshaping 및 인덱싱(면, 행, 열)을 통해
데이터 구조를 이해하는 기초 예제입니다.
"""
import numpy as np
x = np.arrange(2*3*4)
print(x)
x = x.reshape(2,3,4)
print(x)
print("윗면 : ", x[0, :, :]) # ...
print("앞면 : ", x[:, 0, :]) # ...
print("옆면 : ", x[:, :, 0]) # ...
print("1차원으로 : ", x.ravel())