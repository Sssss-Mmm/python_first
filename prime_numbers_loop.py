for n in range(2,10):
     for x in range(2,n):
         if n %x ==0:
             print(n,'equals',x,'*',n//x)
             break
     else:
         # 인수를 찾지 못하고 루프가 종료됨 (소수임)
         print(n,'is a prime number')

for num in range(2,10):
     if num %2 ==0:
         print("Found an even number",num)
         continue
     print("Found a number",num)

def  fib2(n):
    """n까지의 피보나치 수열을 출력합니다."""
    a,b =0,1
    result = []
    while a<n:
        print(a,end=' ')
        result.append(a)
        a,b =b,a+b
    print()
    return result

f100 = fib2(100)
print("result : ",f100)