for n in range(2,10):
     for x in range(2,n):
         if n %x ==0:
             print(n,'equals',x,'*',n//x)
             break
     else:
         # loop fell through without finding a factor
         print(n,'is a prime number')

for num in range(2,10):
     if num %2 ==0:
         print("Found an even number",num)
         continue
     print("Found a number",num)

def  fib2(n):
    """Print a Fibonacci series up to n."""
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