# -*- coding: utf-8 -*-

"""
Step09_Random_Module.py
난수 생성 (Random Module)
"""
import numpy as np

print("=== 1. Random Seed ===")
# 시드를 고정하면 항상 같은 난수가 생성됨 (재현성 확보)
np.random.seed(42)
print("Seed set to 42.")


print("\n=== 2. Generating Random Numbers ===")
# 0 ~ 1 사이의 균등 분포 (Uniform Distribution)
rand_val = np.random.rand(2, 3) # 2x3
print(f"rand (0~1 Uniform):\n{rand_val}")

# 표준 정규 분포 (Standard Normal Distribution, 평균=0, 표준편차가=1)
randn_val = np.random.randn(2, 3)
print(f"randn (Normal Dist):\n{randn_val}")

# 정수 난수 (min, max, size)
randint_val = np.random.randint(1, 100, size=(2, 3)) # 1~99 사이
print(f"randint (1~99):\n{randint_val}")


print("\n=== 3. Shuffle & Choice ===")
data = np.arange(10)
print(f"Original: {data}")

# 섞기 (In-place)
np.random.shuffle(data)
print(f"Shuffled: {data}")

# 랜덤 선택 (Choice)
picked = np.random.choice(data, size=3, replace=False) # 비복원 추출
print(f"Choice (3 items): {picked}")
