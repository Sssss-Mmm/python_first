
"""
[20250414_03.py]
Numpy 배열 생성, 초기화 함수(zeros, ones, full 등) 및 배열 속성 확인 예제입니다.
"""
import numpy as np
import time
print(np.__version__)
#데이터의 개수
n=1000
#피처의 개수
m=10000
#X 행렬의 크기는 1000 * 10000
x= np.random.rand(n,m)
# w 행렬의 크기는 1000 * 1
w= np.random.rand(n,1)

#반복문 사용한 코드
t1 = time.time()
z1= np.zeros((1,m))

for i in range(x.shape[1]):
    for j in range(x.shape[0]):
        z1[0][i] += w[j]*x[j][i]
print("반복문 사용한 코드의 속도 :",(time.time()-t1)*1000,"ms")

#Vectorization 코드
t2=time.time()
z= np.dot(w.T,x)
print("Vectorization 코드의 속도: ",(time.time()-t2)*1000,"ms")