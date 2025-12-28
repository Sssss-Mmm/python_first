# fibonacciModule.py
def fibonacci(n):   
    # n까지의 피보나치 수열 반환
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a,b = b,a+b
    return result