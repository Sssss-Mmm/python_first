import numpy as np
print(np.__version__)

print(np.array([[1,2,3], [4,5,6]]))
print(np.array([2,3,4], dtype="float32"))
temp = np.arange(10)
print(temp)
zeroArray = np.zeros((3,3))
print(zeroArray)
oneArray = np.ones((3,3,3))
print(oneArray)
fullArray = np.full((3,3),3)
print(fullArray)
emptyArray = np.empty((3,3))
print(emptyArray)
print("########## _like test #########")
oneLikeArray = np.ones_like(emptyArray)
print(oneLikeArray)
linSpaceArray = np.linspace(0, 34, 5)
print(linSpaceArray)
a = np.array([[ 0,  1,  2,  3]])
b = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]]) #, dtype='int64')
print(b[2][2])
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.itemsize)
print(b.dtype)
temp = np.array([[[1., 1., 1.],[1., 1., 1.],[1., 1., 1.]],[[1., 1., 1.], 
                    [1., 1., 1.], [1., 1., 1.]], [[1., 1., 1.], [1., 1., 1.], 
                    [1., 0., 1.]]])
print(temp.shape)
print(temp[2,1,2])
print(temp[2][2][1])
print("###### slicing test #######")
a1 = np.array([ 0,  1,  2,  3])
print(a1[:2])
print(a1[1:4:2]) #2 -> step
print(a1[::-1])

print(a[0])
print(a[:2])
print(a[1:4:2]) #2 -> step
print(a[::-1])

print("###### slicing exam #######")

a2 = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7]])
print(a2[0])
print(a2[:2])
print(a2[1:4:2]) #중요
print(a2[::-1]) #중요

print(a2[0,0])
print(a2[:2,0])
print(a2[1:4:2,:]) #중요
print(a2[::-1,:]) #중요
print("########## fancy indexing test start #########")
print(b[[0,2],:])
print(b[0:3:2, :])
print(b[[2,0]])
print(b[-1:-100:-2, :])
print("########## fancy indexing test end #########")
c = np.array([[[0,1,2],[3,4,5]],
              [[6,7,8], [9,10,11]]])
print(c[1, :])

print(b[0,0]) #b[0][0] = 0
print(b[2,1]) #b[2][1] = 9
print(b[[0,2], [0,1]]) # [0,2], [0,1] 이 fancyIndex의 바깥 , 를 기준으로 
                     # 행렬이 나누어져서 0,0 의 위치와 2,1 의 위치 값이 가져온다.

b_5 = b > 5 # b_5 -> filter array
print(b_5)
print(b[b_5])
b[:, [False, True, False, True]]

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
print(a)
b = np.ones_like(a)
print(b)
print(a+b)
print("######## broadcasting #########")
a = np.array([[0], [10], [20], [30]])
b1 = np.array([0,1,2])
b2 = np.array([[0,1,2]])
print(a+b1)
print(a+b2)

c = np.arange(4)
print(c + 1)
print(a + c)
d = np.zeros((2,2,4))
print(d)
print(d+c)

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
newA = np.power(a, 2)
print(newA)

sumRow, sumCol, sumAll = np.sum(a, 
            axis=0), np.sum(a, axis=1), np.sum(a)
print(sumRow)
print(sumCol)
print(sumAll)

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11],
              [12, 13, 14, 15]])
print(a)
print(np.split(a, 2)) 
# 2개로 나눠짐[0, 1][2, 3], axis = 0 (default) row(행)과 vertical이 같은 방향의 의미
print(np.split(a, (1, 3))) 
# 3개로 나눠짐[0][1, 2][3], axis = 0 (default)
split1, split2 = np.vsplit(a, 2) 
# 2개로 나눠짐[0, 1][2, 3], axis = 0 (fixed)
print(split1)
print(split2)

split1, split2 = np.hsplit(a, 2) 
# 2개로 나눠짐[:, 0:2][:, 2:3], axis = 1 (fixed)
print(split1)
print(split2)

stack0 = np.stack((a, a))
# 2개를 합침[0:4][0:4], axis = 0 (default) 아래로 붙음
print(stack0.shape)

stack1 = np.stack((a, a), axis=1)
# 2개를 합침[:, 0:2, :], axis = 1 오른쪽으로 붙음
print(stack1.shape) 

stack2 = np.vstack((a, a))
# 2개를 합침 차원 늘어나지 않음, row가 추가됨
print(stack2.shape) 
# print(stack2) 

stack3 = np.hstack((a, a))
# 2개를 합침 차원 늘어나지 않음, row가 추가됨
print(stack3.shape) 
print(stack3) 
print("#### reshape(), resize() ####")
print(a.shape)
print(a.reshape(2,8))
print(a.reshape(8,2))
# print(a.reshape(3,4)) #...
# print(a.reshape(5,4))
print(a.reshape(8,-1))
# print(a.reshape(-1,-8))
print(a.reshape(16,1))
print(a.resize(2,8))
print(a)
print(a.resize(3,4, refcheck = False)) # refcheck = True
print(np.resize(a,(3,4)))
# print(a.resize(5,4))
# print(a)

print(a.flatten())
print(a)
print(a.ravel())
b = a.ravel()
print("b 출력"); print(b); b[0] = 10
print(a)

a.flatten()[0] = 100 # 복사본의[0] = 100
print("flatten")
print(a) # a[0] == 0 원본은 변경 안됨
a.ravel()[0] = 100 # 참조변수 형태 즉, 원본이 변경
print("ravel")
print(a)

b = np.zeros((1,2,3,4))
print("before", b.shape)
b = b.transpose(0,1,3,2) # 인자(숫자)는 위치
print("after", b.shape)
d = b.T
print(b.shape)
print(d.shape)
print(np.squeeze(b).shape)
print(np.squeeze(d).shape)

a = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11],
              [12, 13, 14, 15]])
print(a[:].shape)
print(a[np.newaxis, :, :].shape)
print(a[:, np.newaxis, :].shape)
print(a[:, :, np.newaxis].shape)