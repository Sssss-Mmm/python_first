### 일처리하는 곳 : (인터페이스) 함수 -> 예외발생시 예외처리 방식이 동일한 경우
def this_fails(n):
    try:
         x =1/n
    except Exception as err:
         print('Handling run-time error:',err) # 예외처리구문

### 호출하는 곳 : 메인 코드 -> 
#                일반적 경우 : 예외발생시 경우에 따라 예외처리 방식이 다를 경우
try:
    #  this_fails(int(input("Please enter a number: ")))
     this_fails(0)
except ZeroDivisionError as err:
     print('Handling run-time error:',err) # 예외처리구문

####################################################

def divide(x,y):
    # 사용자 입력 : (숫자) -> x, y에 입력, 연산... 무한 반복 ... -> Ctrl+C 했을때...
    while True:
        try:
            x =int(input("Please enter first number: "))
            y =int(input("Please enter second number: "))
            result =x/y
        except ZeroDivisionError:
            print("division by zero!")
        except BaseException as err:
            print('Handling run-time error:',err) # 예외처리구문
            raise # 예외처리가 끝나지 않았고, 나를 호출한 측(main함수)에서 나머지를 처리해 달라.
        except :
            print('unknown error') # 예외처리구문
        else:
            print("result is",result)
        finally:
            print("executing finally clause")

divide(2,1)        
divide(2,0)
# divide("2","1")
divide(int("2"),int("0"))
