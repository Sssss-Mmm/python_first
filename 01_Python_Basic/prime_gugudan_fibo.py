"""
[20250409_01.py]
소수 판별, 구구단 출력, 피보나치 수열(함수), 기본 함수 인자 및 스코프 테스트 예제입니다.
"""
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'equals',x,'*',n//x)
            break
    else:
            print(n,'is a prime number')    
for num in range(2,10):
     if num%2 ==0:
          print("Found an even number",num)
          continue
     print("Found a number", num)
     #구구단
for x in range(2,10):     
    for y in range(1,10):
        print(x,"*",y,"=",x*y)

def fib(n):
     a,b=0,1
     while a <n:
          print(a,end=' ')
          a,b=b,a+b
     print()
fib(2000)

f= fib
f(100)
fib(0)
print(fib(0))

def fib2(n):
     result=[]
     a,b=0,1
     while a<n:
          result.append(a)
          a,b =b,a+b
     return result
f100=fib2(100)
print("result: ",f100)

def ask_ok(prompt,retries=4,reminder='Please try again!'):
     while True:
          ok =input(prompt)
          if ok in ('y','ye','yes'):
               return True
          if ok in ('n','no','nop','nope'):
               return False
          retries =retries -1
          if retries <0:
               raise ValueError('invalid user response')
          print(reminder)

# ask_ok("입력:",3,"다시 입력:")

i =5

def f(arg=i):
     print(arg)
     
i = 6
f()

print(i) #전역변수 i
i = 100
f()
def f(a,L=[]):
     L.append(a)
     return L
print(f(1)) # [] -> [1]
print(f(2)) # [1]-> [1,2]->[1,2,2]
print(f(3)) # [1,2,2]-> [1,2,2,3] -> no ->[1,3]

def f(a,L=None):
     if L is None:
          L=[]
     L.append(a)
     return L
print(f(1))
print(f(2))
print(f(3))

def parrot(voltage,state='a stiff',action='voom',type='Norwegian Blue'):
     print("--This parrot wouldn't",action,end=' ')
     print("if you put",voltage,"volts through it.")
     print("-- Lovely plumage,the",type)
     print("--It's",state,"!")
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000,action='VOOOOM')
parrot(action='vOOOOOm',voltage=1000000)
parrot('a million','bereft of life','jump')
parrot('a thousnad',state='pushing up the daisies')
# parrot() #voltage 디폴트값 x
# parrot(voltage=5.0,'dead') # 위치인자로써는 처음이기 때문에 voltage로 인식
# parrot(110,voltage=220) # voltage 값이 다중으로 들어가있음
# parrot(actor='John Cleese') #변수 명이 잘못되어있음
