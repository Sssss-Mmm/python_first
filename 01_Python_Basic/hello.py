 # -*- coding: <UTF-8> -*- 
print("hello")
a = [1, '1', "1"] # 문자열 배열
a = str(a[0]) + a[1] + a[2] # 문자열 - concatenation
b = int(a[0]) + int(a[1]) + int(a[2]) # 정수형으로 바꿔 연산 수행
print(b)
print(8/5) # 실수 나눗셈
print(10/5)
print(8//5) # 정수 나눗셈
i = -1
print(i << 1)
print(i<<2)
print(i>>1)
i = 8
print(i>>3)
print(i>>10)
# language int 32bit
i = 1
print(i<<31) # 31번째 자리는 부호비트 -> -2**31

##################### string #########################
print('spam eggs')
print( 'doesn\'t')  # use \' to escape the single quote...
print(r'C:\some\name') 
print('C:\\some\\name') 
print(3*'ha' + ' smile.')
print( 'Put several strings within parentheses to have' \
' them joined together.')
word = 'Python'
print(word[2:5])
print(word[:2]+word[2:])
# print(word[42])
print(word[4:42])
print(word[42:]) 
# 존재하지 않는 index ~ 끝까지
# str은 불변
# word[0] = 'J'
# word = 'Jython'
word = 'J'+word[1:]
length = len(word)
print(word)
print(length)

# temp = input("입력하세요:")

temp = int(input("숫자를 입력하세요:"))
if temp<0 :
    print("음수를 입력 하셨습니다.")
    print('')
elif temp>0 : 
    print("양수를 입력 하셨습니다.")
else :
    print("Zero 를 입력 하셨습니다.")