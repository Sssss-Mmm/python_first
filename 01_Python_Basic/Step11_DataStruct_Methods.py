# -*- coding: utf-8 -*-

"""
Step08_List_Set_Dict_Methods.py
자료구조 심화 메소드 (Advanced Methods for List, Set, Dictionary)
"""

print("=== 1. List Methods ===")
nums = [1, 2, 3]
print("Original:", nums)

nums.append(4)          # 뒤에 추가
print("Append(4):", nums)

nums.insert(1, 99)      # 인덱스 1에 99 삽입
print("Insert(1, 99):", nums)

pop_val = nums.pop()    # 맨 뒤 요소 꺼내기
print(f"Pop(): {pop_val}, List: {nums}")

nums.remove(99)         # 값으로 삭제
print("Remove(99):", nums)

nums.extend([5, 6])     # 리스트 확장
print("Extend([5, 6]):", nums)

nums.sort(reverse=True) # 정렬
print("Sort(reverse=True):", nums)


print("\n=== 2. Dictionary Methods ===")
info = {"name": "Kim", "age": 25, "city": "Seoul"}

print("Keys:", info.keys())     # Key 목록
print("Values:", info.values()) # Value 목록
print("Items:", info.items())   # (Key, Value) 쌍 목록

# get() 메소드 (KeyError 방지)
print("Get('age'):", info.get("age"))
print("Get('job'):", info.get("job")) # None 반환
print("Get('job', 'Student'):", info.get("job", "Student")) # Default 값 지정

# update()
info.update({"age": 26, "job": "Developer"})
print("Update:", info)


print("\n=== 3. Set Methods ===")
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s1.add(4)
print("Add(4):", s1)

print("Union (합집합):", s1.union(s2))        # s1 | s2
print("Intersection (교집합):", s1.intersection(s2)) # s1 & s2
print("Difference (차집합):", s1.difference(s2))     # s1 - s2
