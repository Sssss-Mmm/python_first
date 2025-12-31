"""
[20250414_01.py]
Python 예외 처리(try-except-else-finally), 사용자 입력 예외 처리 및 사용자 정의 예외 클래스 예제입니다.
"""
import sys
print(dir(sys))

#10 *(1/0) #정수를 0으로 나눌수 없음
# 4+spam*3 #spam이라는 변수가 정의되지않음
# '2'+2 # 

while True:
    try:
        x=int(input("Please entry a number:"))
        break
    except ValueError:
        print("Oops! That was no valid number. Try again...")
    except TypeError:
        print("Oops! That was no valid Type. Try again...")
    except KeyboardInterrupt:
        print("Oops! That was Terminated...")
        break

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass
for cls in [B,C,D]:
    try:
        raise cls()
    except B:
        print("B")
    except D :
        print("D")
    except C:
        print("C")

