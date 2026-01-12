# -*- coding: utf-8 -*-

"""
Step19_Context_Manager.py
Context Manager (with 문)
"""

# with 문을 사용하면 파일을 열고 닫는 것을 자동으로 처리해줍니다.
# 파일뿐만 아니라 Lock, DB 연결 등 리소스 관리에 유용합니다.

print("=== 1. File Handling with 'with' ===")
filename = "example_context.txt"

# 쓰기
with open(filename, "w", encoding="utf-8") as f:
    f.write("Hello, Context Manager!\n")
    f.write("This file allows automatic closing.\n")
print(f"'{filename}' written successfully.")

# 읽기
with open(filename, "r", encoding="utf-8") as f:
    content = f.read()
    print(f"--- File Content ---\n{content}")
# 여기서 f.close()를 호출하지 않아도 자동으로 닫힘


print("\n=== 2. Custom Context Manager (Class) ===")
class MyContext:
    def __enter__(self):
        print(">> Entering Context (Resource Acquired)")
        return self # as 변수에 할당될 객체
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(">> Exiting Context (Resource Released)")
        if exc_type:
            print(f"Error occurred: {exc_val}")
        return False # True를 반환하면 예외를 억제함 (여기선 전파)

with MyContext() as m:
    print("   Inside the block")

print("\n=== 3. Context Manager with Exception ===")
try:
    with MyContext() as m:
        print("   Inside the block (Raising Error)")
        raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"Caught exception outside: {e}")
