"""
[20250411_01.py]
튜플(Tuple), 집합(Set), 딕셔너리(Dictionary) 자료구조 실습 및 외부 모듈(fibonacciModule) 사용 예제입니다.
"""
#del
#리스트 : 요소의 내용 변경 가능
#Mutable : list, dict, set, byte array
#Immutable : tuple, string, integer 등
a=[-1,1,66,25,333,333,1234.5]
del a[0]
print('a=',a)
del a[2:4]
print('a=',a)
del a[:]
print('a=',a)
del a
#- 이터레이트 : 객체의 원소 하나하나에 반복적으로 접근
#- 이터러블 : 자료를 반복할 수 있는 객체. (잠재적으로) 반복가능한 값, 집합데이터지만 변수는 아님(range, map 등)
#- 이터레이터 : 반복가능한 객체로 이루어진 “변수”
#튜플
#문자열,리스트,튜플(이터레이터())
t= 12345,54321,'hello!'
testTuple = "Hello","hi"
#testTuple.append("안녕") #튜플은 문자열처럼 내부의 값을 수정,추가할수 없음
myTuple = 12345,54321,"Hello!"
#다양한 예시#다양한 예시#다양한 예시
print('myTuple[0]=',myTuple[0])   
#12345
print('myTuple=',myTuple)      
#(12345, 54321, 'Hello!')
myTuple_new = myTuple,(1,2,3,4,5)
print("myTuple_new=",myTuple_new)  
#((12345, 54321, 'Hello!'), (1, 2, 3, 4, 5))
# myTuple[0] = 9999   
#튜플은 문자열처럼 내부의 값을 수정,추가할수 없음
v1 = [1,2,3]
v2 = [4,5,6]
vec = (v1,v2)
print('vec=',vec)    #([1,2,3],[4,5,6])
#튜플의 내용은 변경 불가능하나, 변경 가능한 내용물을 튜플에 넣을 순 있음
v1 = [1,3,4]
vec = (v1,v2)
print('vec=',vec)    #([1,3,4],[4,5,6])
print('t[0]=',t[0])
print('t',t)
u= t,(1,2,3,4,5)
print('u',u)
# t[0]=88888 #초기화 x
empty = ()
singleton='hello', # <-- 콤마 생략하면 안됨
print('len(empty)',len(empty))
print(len(singleton))
print(singleton)
myTuple = 12345,"hello",True
#시퀀스 언패킹
x,y,z = myTuple
print("x: ",x," y: ",y," z:",z)
#python - 자료구조: 집합(set)

#- 중복되는 요소가 없고, 순서도 없는 collection(집합데이터)
#- 멤버십 검사와 중복 엔트리제거가 주 용도
    
#    ⇒ 예를들어 평소에 리스트를 사용하다가 중복을 제거하기 위해 list → set 함
    
#    ⇒ 단, set으로 변환하면 순서가 사라짐
    
#- { }, set() 함수로 set을 생성 가능
    
#    ⇒ 단, 비어있는 set은 set()으로 만들어야 하지 {}로 만들면 안됨. {}은 빈 딕셔너리 선언
basket = {"apple","banana","cherry","pear","apple","orange","banana"}
print(basket)
#{'orange', 'banana', 'cherry', 'pear', 'apple'}
#{'cherry', 'banana', 'pear', 'orange', 'apple'}
# 파이썬은 순서가 랜덤하게 바뀜

print("orange" in basket)
#True

print("crabgrass" in basket)
#False

a = set("abracadabra")
print(a)
#{'b', 'r', 'd', 'c', 'a'}
b = set("alhambra castle")
print(b)
#{'m', 'r', 'l', 's', 't', ' ', 'b', 'a', 'e', 'h', 'c'}

print(b-a) #차집합
#{'e', 'm', 't', ' ', 'l', 'h', 's'}

print(a|b) #합집합
#{'e', 'b', 'r', 'a', 'c', 'm', 's', 'd', ' ', 't', 'l', 'h'}

print(a&b) #교집합
#{'r', 'a', 'c', 'b'}

print(a^b)
#{'m', ' ', 't', 'h', 'l', 'e', 's', 'd'}

mySet = {x for x in "abracadabra" if x not in "abc"}

mySet = set()
for x in "abracadabra":
    if x not in "abc":
        mySet.add(x)
print('mySet:',mySet)

#add() : set에 한개의 요소 추가
s1 = set([1,2,3])
s1.add(4)
print('s1:',s1)
#update() : set에 여러개의 요소 추가
s2 = set([1,2,3])
s2.update([4,5,6])
print('s2:',s2)
#remove() : set에서 특정 요소 삭제
s3 = set([1,2,3])
s3.remove(2)
print('s3:',s3)

### python - 자료구조: 딕셔너리(dictionary)

#- 매핑형 자료형
#- 시퀀스 자료형과 달리 숫자로 된 인덱스(index)가 아니라 **키(key)**를 사용함
#    - key로는 모든 불변형을 사용 가능(문자열, 숫자 등)
#    - NULL은 못 들어감 (어떤 언어에서는 가능 - Java의 해시테이블 등)
#    - 튜플이 불변값인 문자열, 숫자, 튜플만 포함할 경우 튜플도 키로 사용할 수 있음
        
#        ⇒ 가변객체인 리스트 이런게 들어있는 튜플 이런건 불가능
        
#     - key는 ‘hashable’ 해야함 ⇒ 고유한 값을 가짐
# - key-value 쌍으로 구성
# - { } 으로 빈 딕셔너리 생성할 수 있음
# - list( {딕셔너리} ) ⇒ 딕셔너리의 모든 키의 리스트를 삽입 순서대로 return함
#     - 키 값을 순서대로 정렬한 리스트를 얻고 싶으면 sorted( {딕셔너리} ) 하면 됨
        
#         ⇒ value들의 리스트를 얻고싶으면 list( {딕셔너리.values()} )

tel  = {"jack":4098,"sape":4139}
tel["guido"] = 4127#다양한 예시
print(tel)
#{'jack': 4098, 'sape': 4139, 'guido': 4127}

print(tel["jack"])
#4098

del tel["sape"]
print(tel)
#{'jack': 4098, 'guido': 4127}

print(list(tel))
#['jack', 'guido']

print(sorted(tel))
#['guido','jack']

print("guido" in tel)
#True

print("jack" not in tel)
#False

print(list(tel.values()))
#[4098, 4127]

myDict = dict([("sape",4139),("guido",4127),("jack",4098)])
print('myDict',myDict)
myDict = dict(sape=4139,guido=4127,jack=4098)
print('myDict',myDict)

myDict = dict()
for x in (2,4,6):
    myDict[x] = x**2
print('myDict',myDict)

myDict = {x:x**2 for x in (2,4,6)}
print('myDict',myDict)

### 딕셔너리 뷰(dictionary view)

# - dictionary view : 딕셔너리의 keys(), values(), items() 등의 메소드가 return하는 객체
    
#⇒ dynamic view라고 해서 주소값만 제공함
    
#⇒ 이터러블(iterable)
    
# - 딕셔너리와 시퀀스를 왔다갔다 하며 루핑(looping) 할 수 있음

knights = {"gallahad":"the pure","robin":"the brave"}
for key,value in knights.items():
	print('key= ',key,',value=',value)
     
for x,y in enumerate(['tic','tac','toe']):
	print(x,y)
      
#   zip(seq1,seq2)로 둘 이상의 시퀀스를 합쳐서 루핑    
questions = ["name","quest","favorite color"]
answers = ["lancelot","the holy grail","blue"]
for question,answer in zip(questions,answers):
	print("What is your {0}? It is {1}.".format(question,answer))      
# - 시퀀스 정렬 함수들
#     - reversed() ⇒ 원본을 변경하지 않고 역으로 정렬된 시퀀스를 리스트로 받을 수 있음
#     - sorted() ⇒ 원본을 변경하지 않고 정렬된 시퀀스를 리스트로 받을 수 있음
#         - sorted(set(List)) : 중복을 제거하고 정렬된 리스트로 반환    

### 조건문과 비교

# - where, if 등에서
#     - in, not in ⇒ 값이 시퀀스에 있는지 검사
#     - is, is not ⇒ 두 객체가 진짜로 같은 객체인지 비교

# ---

# - 비교연산자는 연쇄 가능
#     - a < b == c
        
#         a가 b보다 작은지 && b와 c가 같은지
        
#     - 서로 우위가 없음 ⇒ 왼쪽에서 오른쪽으로 진행
        
a = True
b = False
c = True
         
a and b and c
        
        # a and b 먼저 계산해서 False가 나으므로 c는 고려도 안함
        



# - 표현식에서의 대입은 바다코끼리 연산자 (:=)로 수행해야 함
    

str1,str2,str3 = None,"Hammer Dance","Trondheim"
non_null = str1 or str2 or str3
print(non_null)

### 시퀀스와 다른 타입들을 비교

# - 시퀀스끼리 비교할 때는 맨 첫 요소부터 차례로 사전식 순서로 비교
    
#     (1,2,4) < (1,2,5)
    
#     (1,2,3,4) < [1,2,4]
    
#     (1,2,(’apache’,’bwapp’)) < (1,2,(’tomcat’,’honeypot’),4)
    
# - 모든 요소가 서로 같으면 먼저 소진된 쪽이 작은 것
    
#     (1,2,3,4) < (1,2,3,4,5,6)
    
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end='')
        a,b = b,a+b
    print()
    
def fib2(n):
    result = []
    a,b= 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result


resultList = fib2(1000)
print('resultList: ',resultList)
print("-----------------------------")

import Step10_Module_Custom as fib3
print(fib3.__name__)
resultList[:] = []
resultList = fib3.fibonacci(1000)
print(resultList)

# import -> 동적 라이브러리 호출(dll)
# include -> (C, C++언어) 정적 라이브러리 호출(sll)
# import tensorflow
# print(tensorflow.__name)

from Step10_Module_Custom import fibonacci as fib4
print(fib4(100))
# 'python.exe' 'launcher' '51071'(메모리주소) -- 20250411_01.py(파일명)
# dir(fibonacci) #import
print(dir(fib4))
