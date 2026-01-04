import sys
# f =open('C:/Users/user/Desktop/myfile.txt')
i = 0
try:
    f =open('myfile1.txt')
    s =f.readline()
    i =int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:",sys.exc_info()[0])
    raise
else:   # try - else 사용
    print(arg,'has',len(f.readlines()),'lines')
    f.close()

print(i)

for arg in sys.argv[1:]:
    try:
        f =open(arg,'r') #rwx
        print(f)
    except OSError:
        print('cannot open',arg)
    else:
        print(arg,'has',len(f.readlines()),'lines')
        f.close()

try:
    raise Exception('spam','eggs') # 익명 클래스 -> 객체 생성
except Exception as inst:
    print(type(inst))    # 예외 인스턴스
    print(inst.args)     # .args에 저장된 인자들
    print(inst)          # __str__ 메서드를 통해 인자를 직접 출력할 수 있음,                         
                         # 하지만 예외 하위 클래스에서 오버라이딩 될 수 있음
    x,y =inst.args       # 인자 언패킹
    print('x =',x)
    print('y =',y)
    