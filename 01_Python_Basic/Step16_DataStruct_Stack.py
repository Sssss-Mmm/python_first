tel2 = {}
tel ={'jack':4098,'sape':4139}
# tel2 = dic()
dict(sape=4139,guido=4127,jack=4098)
dict([('sape',4139),('guido',4127),('jack',4098)])
lis = []
lis.sort()
# sorted()

basket =['apple','orange','apple','pear','orange','banana']
for f in sorted(set(basket)):
   print(f)
a,b,c = 0,0,0
a < b == c
(a < b) and (b == c)
#  a 가 b 보다 작고, 동시에 b 가 c 와 같은지 검사합니다.

(a < b) == c

A,B,C = 0,0,0
A and (not B) or C
# A는 B이거나 C가 같지 않느냐? -> 틀림
(A and (not B)) or    C 

A and B or C  # 논리곱과 논리합의 결합 -> * 와 +로 대체해서 확인
(A and B) or C 
A * B + C

if (1,2,('aa','ab')) < (1,2,('abc','a'),4) :
   print("true")

# while True:
#    pass

# while -100:
#    pass

dir(lis)