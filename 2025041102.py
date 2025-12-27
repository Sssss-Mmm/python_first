# Fibonacci numbers module
def fib(n):    # write Fibonacci series up to n
    a,b = 0,1
    while a<n:
        print(a,end=' ')
        a,b = b,a+b
    print()

fib(1000)

def fib2(n):   # return Fibonacci series up to n
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result
resultList = fib2(1000)
print(resultList)
print("######################")

import fibonacciModule as fib3
print(fib3.__name__)
resultList[:] = []
resultList = fib3.fibonacci(1000)
print(resultList)

# import -> 동적 라이브러리 호출(dll)
# include -> (C, C++언어) 정적 라이브러리 호출(sll)
# import tensorflow
# print(tensorflow.__name)

from fibonacciModule import fibonacci as fib4
print(fib4(100))

# dir(fibonacci)
dir(fib4)
