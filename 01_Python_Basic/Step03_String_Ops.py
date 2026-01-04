# -*- coding: utf-8 -*-

"""
Step03_String_Ops.py
문자열 조작 (String Operations)
"""

s = "Hello, Python World!"

print("=== 1. Basic Methods ===")
print("Original:", s)
print("Upper:", s.upper())      # 대문자로 변환
print("Lower:", s.lower())      # 소문자로 변환
print("Replace:", s.replace("Python", "Coding")) # 문자열 치환
print("Split:", s.split(","))   # 구분자로 나누기 (List 반환)

print("\n=== 2. Indexing & Slicing ===")
# Indexing (0부터 시작)
print("s[0]:", s[0])
print("s[7]:", s[7])
print("s[-1]:", s[-1]) # 뒤에서 첫 번째

# Slicing [start:end:step]
print("s[0:5]:", s[0:5])   # "Hello" (0~4)
print("s[7:]:", s[7:])     # "Python World!" (7부터 끝까지)
print("s[:5]:", s[:5])     # "Hello" (처음부터 4까지)
print("s[::2]:", s[::2])   # "Hlo yhnWrd" (2칸씩 건너뛰기)
print("s[::-1]:", s[::-1]) # "!dlroW nohtyP ,olleH" (역순)

print("\n=== 3. String Formatting ===")
name = "Alice"
age = 30

# f-string (Python 3.6+) - 권장 방식
print(f"My name is {name} and I am {age} years old.")

# format() method
print("My name is {} and I am {} years old.".format(name, age))

# % operator (Old style)
print("My name is %s and I am %d years old." % (name, age))

print("\n=== 4. Other Useful Functions ===")
s2 = "   strip example   "
print(f"'{s2}' -> strip() -> '{s2.strip()}'") # 양쪽 공백 제거

join_list = ['A', 'B', 'C']
print("Join:", "-".join(join_list)) # "A-B-C" 
