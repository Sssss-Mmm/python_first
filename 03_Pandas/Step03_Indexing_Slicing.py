"""
[20250416_01.py]
Numpy 다차원 배열 접근 및 Matplotlib을 이용한 다양한 그래프(Line, Bar, Scatter, Box, Pie, Histogram) 시각화 예제입니다.
"""
import numpy as np
x= np.arange(2*3*4)
print("x = np.arange(2*3*4):\n",x);print()

x= x.reshape(2,3,4)
print("3차원으로 변환(axis 0 ,axis 1, axis 3):\n",x);print()

print("첫번째 평면 선택(plans):\n",x[0,:,:]);print()
print("첫번째 행 선택(plans):\n",x[:,0,:]);print()
print("첫번째 열 선택(plans):\n",x[:,:,0]);print()

print("x.ravel():\n",x.ravel())

import matplotlib.pyplot as plt

plt.figure()
x=np.array([1,2,3,4])  
y=np.array([2,4,6,8])  
# plt.plot(x)
# plt.plot(y)
# plt.plot(x,x**2)
# x=np.arange(0,5,0.2)
# plt.plot(x,x**2,"ro")
# plt.plot(x,x**3,"b^")
# plt.plot(x,x**4,"gs")
# plt.show()

# x=np.array([1,2,3,4])
# y=np.power(x,2)
# plt.bar(x,y) 

# plt.show()
# plt.barh(x,y)

# np.random.seed(50) #rand()가 동일한 결과를 나오도록 함
# x=np.random.rand(50)
# y=(x * 10) + np.random.rand(50)
# plt.scatter(x,y)

# np.random.seed(0)
# spread = np.random.rand(50)* 100
# center = np.ones(25)* 50
# flier_high = np.random.rand(10) * 100 +100
# flier_low = np.random.rand(10) * 100 - 100
# data = np.concatenate((spread,center,flier_high,flier_low))
# plt.boxplot(data)

# data = np.array([1,2,3,4])
# labels = ["A","B","C","D"]
# plt.pie(data,labels=labels)
# np.random.seed(0)
# mu, sigma = 100,15
# data= mu+sigma* np.random.randn(10000)
# plt.hist(data)

# x1= np.arange(5)
# x2= np.power(x1,2)
# x3= np.power(x1,3)
# plt.style.use("ggplot")
# plt.plot(x1,color="red",marker="o",linestyle="None")
# plt.plot(x2,color="blue",marker="s",linestyle="None")
# plt.plot(x3,color="green",marker="^",linestyle="None")
# plt.title("title")
# plt.xlabel("x-label")
# plt.ylabel("y-label")
# # plt.grid()
# plt.xticks([0,2,4])
# plt.yticks([0,30,60])
# plt.legend(["x1","x2","x3"])
# for feature in [x1,x2,x3]:
#     for i,data in enumerate(feature):
#         plt.text(i,data+1.5,data)
# print(plt.style.available)
import matplotlib.font_manager as fm
import matplotlib as mat
for font in fm.fontManager.ttflist:
    print(font.name)
font1=mat.rcParams["font.family"]="NanumGothic"

x= np.arange(4)
plt.subplot(2,2,1)
plt.plot(x,x)
plt.title("한글 그래프1")
plt.subplot(2,2,2)
plt.plot(x,x**2, color="red")
plt.title("한글 그래프2")
plt.subplot(2,2,3)
plt.plot(x,x**3, color="green")
plt.title("한글 그래프3")
plt.subplot(2,2,4)
plt.plot(x,x**4, color="black")
plt.title("한글 그래프4")
cat= plt.imread("python_first\cat1.jpg")
plt.imshow(cat)
plt.show()