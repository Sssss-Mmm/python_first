import numpy as np
import time
n=1000
m = 10000
x = np.random.rand(n,m)
w = np.random.rand(n,1)

t1 = time.time()
z1 = np.zeros((1,m))
for i in range(x.shape[1]):
    for j in range(x.shape[0]):
        z1[0][i] += w[j]*x[j][i]
print("반복문 사용 코드의 속도 : ", (time.time()-t1)*1000, "ms")

t2 = time.time()
z = np.dot(w.T, x)
print("Vectorization 코드의 속도 : ", (time.time()-t2)*1000, "ms")