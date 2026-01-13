# -*- coding: utf-8 -*-

"""
Step07_Aggregation.py
집계 함수 (Aggregation: Sum, Mean, Min, Max, etc.)
"""
import numpy as np

arr = np.arange(1, 13).reshape(3, 4)
print(f"Array:\n{arr}")

print("\n=== 1. Basic Aggregation ===")
print(f"Sum (Total): {np.sum(arr)}")
print(f"Mean (Average): {np.mean(arr)}")
print(f"Max: {np.max(arr)}")
print(f"Min: {np.min(arr)}")
print(f"Std (Standard Deviation): {np.std(arr):.2f}")


print("\n=== 2. Aggregation with Axis ===")
# axis=0: 열(Column) 기준 연산 (세로 방향 압축)
sum_cols = np.sum(arr, axis=0)
print(f"Sum axis=0 (Columns): {sum_cols}")

# axis=1: 행(Row) 기준 연산 (가로 방향 압축)
mean_rows = np.mean(arr, axis=1)
print(f"Mean axis=1 (Rows): {mean_rows}")


print("\n=== 3. Argmin & Argmax ===")
# 최솟값, 최댓값의 '인덱스' 반환
data = np.array([10, 50, 20, 80, 30])
print(f"Data: {data}")
print(f"Argmax Index: {np.argmax(data)}") # 80의 위치인 3
print(f"Argmin Index: {np.argmin(data)}") # 10의 위치인 0
