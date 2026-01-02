"""
Advanced Python Features Example
--------------------------------
이 파일은 Python의 중급/고급 기능을 다룹니다.
1. Decorators (데코레이터): 함수의 실행 시간을 측정하는 기능 추가.
2. Context Managers (컨텍스트 매니저): 리소스(파일, DB 연결 등)의 안전한 관리를 위한 클래스.
3. Generators (제너레이터): 대용량 데이터를 효율적으로 처리하기 위한 반복자.
"""

import time
import random
from contextlib import contextmanager

# ---------------------------------------------------------
# 1. Decorators: 실행 시간 측정
# ---------------------------------------------------------
def timer_decorator(func):
    """함수의 실행 시간을 측정하여 출력하는 데코레이터"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[Start] '{func.__name__}' 함수 실행 시작")
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[End] '{func.__name__}' 실행 완료 (소요 시간: {end_time - start_time:.4f}초)")
        return result
    return wrapper

@timer_decorator
def heavy_computation():
    """시간이 걸리는 작업을 시뮬레이션"""
    print("  ... 복잡한 계산 수행 중 ...")
    time.sleep(1.5) # 1.5초 대기
    return "계산 완료"

# ---------------------------------------------------------
# 2. Context Managers: 사용자 정의 'with' 구문 
# ---------------------------------------------------------
class MyResource:
    """리소스를 열고 닫는 것을 관리하는 클래스 예제"""
    def __enter__(self):
        print("\n[Resource] 리소스를 할당합니다 (연결/파일열기 등).")
        return self

    def do_something(self):
        print("  [Resource] 작업을 수행합니다.")

    def __exit__(self, exc_type, exc_value, traceback):
        print("[Resource] 리소스를 안전하게 해제합니다 (연결종료/파일닫기).")
        if exc_type:
            print(f"  -> 예외 발생 감지: {exc_value}")
        # True를 반환하면 예외를 무시함, False면 예외 전파

# ---------------------------------------------------------
# 3. Generators: 대용량 데이터 처리 (메모리 절약)
# ---------------------------------------------------------
def infinite_sequence_generator():
    """무한한 숫자 시퀀스를 생성하는 제너레이터 (메모리에 모든 숫자를 저장하지 않음)"""
    num = 0
    while True:
        yield num
        num += 1

def data_stream_simulation(n):
    """n개의 데이터를 하나씩 '생성'하여 반환"""
    print(f"\n[Generator] {n}개의 데이터 스트림 처리 시작...")
    for i in range(n):
        # 복잡한 데이터를 생성한다고 가정
        data = f"Data-packet-{i}"
        yield data 

# ---------------------------------------------------------
# 메인 실행
# ---------------------------------------------------------
if __name__ == "__main__":
    print("=== 1. Decorator Test ===")
    result = heavy_computation()
    print(f"  Result: {result}")

    print("\n=== 2. Context Manager Test ===")
    with MyResource() as resource:
        resource.do_something()
    
    print("\n=== 3. Generator Test ===")
    gen = data_stream_simulation(5)
    for item in gen:
        print(f"  Received: {item}")
        time.sleep(0.3) # 데이터 처리 시간 시뮬레이션
