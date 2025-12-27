"""
[20250410_01.py]
함수 인자(위치/키워드 전용), 람다(lambda) 함수, 리스트/스택/큐 구현, 리스트 컴프리헨션(List Comprehension) 및 행렬 전치 예제입니다.
"""
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg,/):
    print(arg)

def kwd_only_arg(*,arg):
    print(arg)
def combined_example(pos_only,/,standard,*,kwd_only):
    print(pos_only,standard,kwd_only)

standard_arg(123)
pos_only_arg(123) # / 뒤는 위치 인자만 가능
kwd_only_arg(arg=123) # * 뒤에 오는 인자는 키워드로만 가능
combined_example(123,123,kwd_only=123) # * 뒤에 오는 인자는 키워드 인자만 가능

def foo(name,/,**kwds):
    return 'name'in kwds

foo(1,**{'name':2})

def write_multiple_items(file,separator,*args): #* 하나는 list,set **는 집합 map 
    file.write(separator.join(args)) 
    print(separator.join(args))
def concat(*args,sep="/"):
    return print(sep.join(args))
concat("earth","mars","venus")
concat("earth","mars","venus",sep=".")

print(list(range(3,6)))

arg= [3,6]
for a in arg :
    print(a)
print(list(range(*arg)))

def parrot(voltage,state='a stiff',action='voom'):
    print("-- This parrot wouldn't",action,end=' ')
    print("if you put",voltage,"volts through it",end=' ')
    print("E's",state,"!")
d={"voltage":"four million","state":"bleedin' demised","action":"VOOM"}
parrot(**d)

def add(a,b):
    return a+b
print(add(1,2))

foo = lambda a,b: a+b
print(foo(1,2))

def make_incrementor(n): #configuration 설정값 필요
    return lambda x: x+n
make_incrementor(10) #10 -> n
f= make_incrementor(10) #n에 1 0이 저장된 make_incrementor 함수가 f라는 함수명에 alias 지정 


print(f(0)) # 0 -> x
print(f(1))

l =[1,4,3,2]
l.sort()
print(l)

pairs = [(1,'one'),(2,'two'),(3,'three'),(4,'four')]

pairs.sort(key=lambda pair:pair[1],reverse=True) # pair[0]= 1,2,3,4 # pair[1]=one,two,three,four

print(pairs)

def f(ham:str,eggs:str='eggs')->str:
    print("Annotations:",f.__annotations__)
    print("Arguments:",ham,eggs)
    return ham + ' and '+ eggs
print(f('spam'))

fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))
print(fruits.index('banana',4))
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
stack=[3,4,5]
stack.append(6)
stack.append(7)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

from collections import deque
queue = deque(["Eric","John","Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft()) #Eric left
print(queue.popleft()) #John left
print(queue)
squares= []
for x in range(10):
    squares.append(x**2)
print(squares)

squares=list(map(lambda x:x**2,range(10)))
print(squares)

squares=[x**2 for x in range(10)]
squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)

print([(x,y)for x in [1,2,3]for y in[3,1,4]if x != y])

combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print(combs)

vec=[-4,-2,0,2,4]
print([x*2 for x in vec])
print([x for x in vec if x>=0])
print([abs(x) for x in vec])
freshfruit = [' banana',' loganberry','passion fruit ']
print([w.strip() for w in freshfruit])
print([(x,x**2) for x in range(6)])
# print([x,x**2 for x in range(6)]) # x,x**2

vec = [[1,2,3],[4,5,6],[7,8,9]]
print(vec[1][2])
print([n for e in vec for n in e])

a=[]
for e in vec :
    for n in e:
        a.append(n)
print(a)

from math import pi
s=[str(round(pi,i)) for i in range(1,6)]
print(s)

b= []
for i in range(1,6):
    b.append(str(round(pi,i)))
print(b)

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m= [[row[i]for row in matrix]for i in range(4)]
print(m)

transposed=[]
for i in range(4):
    transposed.append([m[i] for m in matrix])
print(transposed)
print(list(zip(*matrix)))

