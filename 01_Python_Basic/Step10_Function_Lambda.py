# -*- coding: utf-8 -*-

"""
Step10_Function_Lambda.py
Lambda 함수와 유용한 내장 함수 (Lambda, Map, Filter, Zip, Enumerate)
"""

print("=== 1. Lambda Function ===")
# lambda arguments: expression
add = lambda x, y: x + y
print(f"Lambda add(10, 20): {add(10, 20)}")

square = lambda x: x ** 2
print(f"Lambda square(5): {square(5)}")


print("\n=== 2. Map (map) ===")
# 리스트의 모든 요소에 함수를 적용
nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x**2, nums))
print(f"Original: {nums}")
print(f"Squared (map): {squared_nums}")


print("\n=== 3. Filter (filter) ===")
# 조건에 맞는 요소만 걸러냄
evens = list(filter(lambda x: x % 2 == 0, nums))
print(f"Evens (filter): {evens}")


print("\n=== 4. Zip (zip) ===")
# 두 개 이상의 리스트를 병렬로 묶음
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
zipped = list(zip(names, ages))
print(f"Zipped: {zipped}")

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")


print("\n=== 5. Enumerate (enumerate) ===")
# 인덱스와 값을 동시에 반환
fruits = ["Apple", "Banana", "Cherry"]
print(f"Fruits: {fruits}")

for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")
