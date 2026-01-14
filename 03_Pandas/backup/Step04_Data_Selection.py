"""
[Step 04] Matplotlib Visualization Basics
-----------------------------------------
Matplotlib을 이용한 다양한 그래프 시각화 및 한글 폰트 설정 예제입니다.
Line, Scatter, Bar, Pie Chart 및 Subplot 사용법을 다룹니다.
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4])
# plt.plot(x)
# plt.show()
# y = np.array([2,4,6,8])
# plt.plot(y)
# plt.show()
# plt.plot(x, x**2)
x = np.arange(0, 5, 0.2)
# plt.plot(x, x**2, "or")
# plt.plot(x, x**3, "b^")
# plt.plot(x, x**4, "gs")

x = np.array([1,2,3,4])
y = np.power(x, 2)
# plt.bar(x,y)
# plt.show()
# plt.barh(x,y)

# np.random.seed(0) 
# rand()가 동일한 결과를 나오도록 함.
# x = np.random.rand(50)
# y = (x * 10) + np.random.rand(50)
# plt.scatter(x, y)

# data = np.array([1,2,3,4])
# labels = ["A", "B", "C", "D"]
# plt.pie(data, labels=labels)

# plt.title("PIE Chart")
# plt.xlabel("x label")
# plt.ylabel("y label")
# plt.grid()
# plt.xticks([0,2,4])
# plt.xticks([0,30,60])
# plt.legend(["x1","x2","x3"])
# plt.show()

x1 = np.arange(5)
x2 = np.power(x1, 2)
x3 = np.power(x1, 3)
x4 = np.power(x1, 4)

# plt.style.use("ggplot")
# plt.plot(x1, "ro", x2, "bs", x3, "g^")
# plt.title("PIE Chart")
# plt.xlabel("x label")
# plt.ylabel("y label")
# # plt.grid()
# plt.xticks([0,2,4])
# plt.yticks([0,30,60])
# plt.legend(["x1","x2","x3"])
# for feature in [x1, x2, x3]:
#     for i, data in enumerate(feature):
#         plt.text(i, data+1.5, data)

# print(plt.style.available)


import matplotlib.font_manager as fm
for font in fm.fontManager.ttflist : 
    print(font.name)
# fm.rcParams["font.family"] = "MagunGothic" 
# font1 = plt.rcParams   
plt.rcParams["font.family"] = "NanumGothic"

# fname 옵션을 사용하는 방법(ttf, otf, ...)
# path = '/Library/Fonts/NanumGothic.otf'
# fontprop = fm.FontProperties(fname=path, size=18)

# print(font_name)
# plt.rc('font', family='NanumGothic')

# plt.subplot(2,2,1)
# plt.plot(x1,x1)
# plt.title("한글 그래프1")
# plt.subplot(2,2,2)
# plt.plot(x1,x2, color='red')
# plt.title("한글 그래프2")
# plt.subplot(2,2,3)
# plt.plot(x1,x3, color='green')
# plt.title("한글 그래프3")
# plt.subplot(2,2,4)
# plt.plot(x1,x4, color='blue')
# plt.title("한글 그래프4")

cat = plt.imread("cat.jpg")
print(cat)
plt.imsave("savedCat.png", cat)
plt.imshow(cat)




plt.show()