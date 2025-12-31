import sys
f=open('c:/Users/hi/Desktop/myfile.txt')
s=f.readline()
i=0
try:
    i=int(s.strip())
    print('i',i)
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError: #
    print("Could not convert data to an integer.")
except: # 예상하지 못한 에러가 발생했을시
    print("Uncexpected error:",sys.exc_info()[0])
    raise
else:
        print('has', len(f.readlines()), 'lines')
        f.close()

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
        print(f)
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x,y =inst.args
    print('x =',x)
    print('y =',y)
# 일처리하는 곳: (인터페이스) 함수
def this_fails(n):
        x= 1/n
# 호출하는 곳 : 메인 코드
try:
    this_fails(0)
except ZeroDivisionError as err:
    print('Handling run-time error:',err)

# try:
#  raise KeyboardInterrupt
# finally:
#  print('Goodbye, world!') #에러가 발생해도 출력이 됨

def divide(x,y):
     try:
        result= x/y
     except ZeroDivisionError:
        print("division by zero")
     else:
         print("result is",result)
     finally:
         print("execusting finally clause")
print(divide(2,1))
print(divide(2,0))
# print(divide('2','1')) # 문자열 타입은 x
print(divide(int("2"),int("1")))
print(divide(int("2"),int("0")))
# 호지차
# 사용자 입력 : (숫자) -> x,y에 입력, 연산... 무한 반복 ... -> ctrl+c 햇을때
while True:
    try:
        x=int(input('x: '))
        y=int(input('y: '))
        result= x/y
    except ZeroDivisionError:
        print("division by zero")
    # except BaseException as err:
    #     print("Handling run-time error: ",err)
    #     raise # 예외처리 끝나지 않았고, 나를 호출한 측(main함수)
    # except:
    #     print('unknown error') #예외처리구문       
    else:
         print("result is",result)
    finally:
         print("execusting finally clause")


