"""
[20250415_01.py]
Numpy 배열 슬라이싱, 팬시 인덱싱, 브로드캐스팅, 배열 변환(Shape manipulation) 예제입니다.
"""
import numpy as np
print(np.__version__)

print(np.array([[1,2,3],[4,5,6]]))
print(np.array([2,3,4],dtype=("float32")))
temp = np.arange(10)
print(temp)
za=np.zeros((3,3))
print(za)
oa = np.ones((3,3,3))
print(oa)
fa=np.full((3,3,3),2)
print(fa)
ema=np.empty((2,3))
print(ema)
print("-----------------_like test------------------")
a= np.array(temp)
print(np.ones_like(a))
linSpaceArray= np.linspace(0,30,5)
print(linSpaceArray)
b= np.array([[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11]],dtype=('int32'))
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.itemsize)
print(b.dtype)
print(b.strides)
temp1=np.array([[[1., 1.,1.],
  [1., 1., 1.],
  [1., 1., 1.]],[[1., 1.,1.],
  [1., 1., 1.],
  [1., 1., 1.]],[[1., 1.,1.],
  [1., 1., 1.],
  [1., 0., 1.]]])
print(temp1.shape)
print(temp1[2][2][1])
print(temp1[2,1,2])
a=np.array([[0,1,2,3]])
b=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(b[2][2])
print("-------slicing test----------")
a1=np.array([0,1,2,3])
a2=np.array([[0,1,2,3],[4,5,6,7]])
print(a1[:2])
print(a1[1:4:2])
print(a1[::-1])

print(a[0])
print(a[:2])
print(a[1:4:2])
print(a[::-1])

print(a2[0])
print(a2[:2])
print(a2[1:4:2])
print(a2[::-1,::-1]) 

c=np.array([[[0,1,2],[3,4,5]],[[6,7,8],[9,10,11]]])
print(c[1,:])
print(b[-1::-2,:])# reverse ,2칸 간격

print("--------------fancy indexing---------------")
print(b[[0,2],:])
print(b[[2,0],:])
print(b[0,0])
print(b[2,1])
print(b[[0,2],[0,1]]) # b[[ㄱ,ㄴ],[ㄷ,ㄹ]] 1번째묶음(ㄱ,ㄷ) 2번째묶음(ㄴ,ㄹ)
print(b[[0,0],[2,1]])
b_5 = b>5 #b_5 filter array
print(b_5)
print(b[b_5])
print(b[:,[False,True,False,True]])
a= np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
b=np.ones_like(a)
print(b)
print(a+b)
print("----------------broadcasting--------------")
a=np.array([[0],[10],[20],[30]])
b=np.array([0,1,2])
print(a+b)
c= np.arange(4)
print(c+1)
print(a+c)
d=np.zeros((2,2,4))
print(d)
print(d+c)
a= np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11]])
print(np.power(a,2))
sumRow,sumCol,sumAll=np.sum(a,axis=0),np.sum(a,axis=1),np.sum(a)

print(sumRow,sumCol,sumAll)

a = np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
print(a)
print(np.split(a,2)) # 2개로 나눠짐[0,1][2,3]
print(np.split(a,(1,3))) # 3개로 나눠짐 [0],[1,2][3]

split1,split2 = np.vsplit(a,2)
#2개로 나눠짐[0,1],[2,3], axis =0 (fixed)
print("split1",split1)
print("split2",split2)
split1,split2 = np.hsplit(a,2)
# 2개로 나눠짐[:,0:2][:,2:3], axis = 1(fixed)
print("split1",split1)
print("split2",split2)
stack0 = np.stack((a,a))
#2개를 합침[0:4][0,4], axis =0 (default) 아래로 붙음
print("-------stack------------")
print(stack0.shape)
print(stack0)
stack1 = np.vstack((a,a))
print(stack1.shape)
print(stack1) #합쳐지지만 차원이 달라지지 않음

print("-------reshape,resize------------")
print(a.shape)
print(a.reshape(2,8))
print(a.reshape(8,2))
# print(a.reshape(3,4))
# print(a.reshape(5,4))
print(a.reshape(8,-1))
print(a.reshape(1,16))
a.resize(2,8)
print(a)
print(a.resize(3,4,refcheck=False))
print("------")
print(np.resize(a,new_shape=(3,4)))
print("-------flatten,ravel------------")
a.flatten()[0]=100 #복사본의[0] = 100
print("flatten")
print(a) #a[0]= 0 원본은 변경 안됨
a.ravel()[0]=100 #참조변수 형태 즉, 
print("ravel")
print(a)
b = a.ravel()
print("b 출력"); print(b); b[0]=10
print(a)
# transpose
print("-------transpose------------")
b= np.zeros((1,2,3,4))
print("before",b.shape)
c=b.transpose(0,1,3,2)
print("after",c.shape)
d = b.T
print(d.shape)
print("-------squeeze------------")
print(np.squeeze(b).shape)
print(np.squeeze(d).shape)
print("-------------newaxis-----------")
print(a[:].shape)
print(a[np.newaxis,:,:].shape)
print(a[:,np.newaxis,:].shape)
print(a[:,:,np.newaxis].shape)
