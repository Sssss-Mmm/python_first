"""
[fibonacciModule.py]
다른 스크립트에서 import하여 사용할 수 있는 피보나치 수열 생성 함수 모듈입니다.
"""
# fibonacci.py
def fibonacci(n):   
    # return Fibonacci series up to n
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result