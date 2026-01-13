# -*- coding: utf-8 -*-

"""
Step02_DataTypes.py
자료형과 형변환 (Data Types & Casting)
"""
import numpy as np

print("=== 1. Specifying Data Types ===")
# 생성 시 dtype 지정
f_arr = np.array([1, 2, 3], dtype=float)
print(f"Float Array: {f_arr}, dtype: {f_arr.dtype}")

i_arr = np.array([1.5, 2.7, 3.9], dtype=int) # 소수점 버림
print(f"Int Array: {i_arr}, dtype: {i_arr.dtype}")


print("\n=== 2. Type Conversion (astype) ===")
# 이미 생성된 배열의 타입 변경
arr = np.array([1.1, 2.2, 3.3])
print(f"Original: {arr}, dtype: {arr.dtype}")

# float -> int
arr_int = arr.astype(int) # 또는 np.int32, np.int64
print(f"Converted to Int: {arr_int}, dtype: {arr_int.dtype}")

# int -> str
arr_str = arr_int.astype(str) # 유니코드 문자열
print(f"Converted to String: {arr_str}, dtype: {arr_str.dtype}")

# str -> float
arr_str_nums = np.array(["1.5", "2.6", "3.7"])
arr_float_recovered = arr_str_nums.astype(float)
print(f"String to Float: {arr_float_recovered}")
