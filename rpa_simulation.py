import csv
import os
import random
from datetime import datetime

# ---------------------------------------------------------
# [RPA 시나리오 시뮬레이션]
# 시나리오: "매일 아침 전날 매출 데이터를 읽어서, 부서별 합계를 내고, 요약 파일을 생성한다."
# RPA 툴(Brity RPA 등)이 하는 일을 Python 로직으로 구현한 예시입니다.
# 면접에서 "이러한 로직을 RPA 툴로 구현하거나, 복잡한 부분은 Python으로 처리할 수 있다"고 어필하세요.
# ---------------------------------------------------------

# 1. [가상 데이터 생성] (RPA가 시스템에서 다운로드 받았다고 가정)
def create_dummy_daily_report(filename):
    departments = ["영업1팀", "영업2팀", "영업3팀", "마케팅팀"]
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["날짜", "부서", "매출액", "담당자"]) # 헤더
        
        for _ in range(20): # 20건의 데이터 생성
            date = datetime.now().strftime("%Y-%m-%d")
            dept = random.choice(departments)
            amount = random.randint(100, 1000) * 10000 # 100만 ~ 1000만
            manager = f"담당자_{random.randint(1, 10)}"
            writer.writerow([date, dept, amount, manager])
    print(f"[Step 1] '{filename}' 파일 다운로드 완료 (가상)")

# 2. [데이터 읽기 및 가공] (RPA의 'Read Excel', 'Loop', 'Calculate' 단계)
def process_report(input_file, output_file):
    summary = {} # 부서별 매출 합계 저장
    
    print(f"[Step 2] '{input_file}' 데이터 읽기 및 집계 중...")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            dept = row["부서"]
            amount = int(row["매출액"])
            
            if dept in summary:
                summary[dept] += amount
            else:
                summary[dept] = amount
    
    # 3. [결과 저장] (RPA의 'Write Excel', 'Send Email' 단계)
    print(f"[Step 3] 집계 결과 '{output_file}' 생성 중...")
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["부서", "총매출액", "비고"])
        
        for dept, total in summary.items():
            # 매출 5000만원 이상이면 '우수' 표시 (조건 분기 로직)
            note = "목표 달성" if total >= 50000000 else "노력 요망"
            writer.writerow([dept, total, note])
            
    print("[Complete] 모든 작업이 완료되었습니다.")
    print(f" -> 결과 파일: {output_file}")

# 메인 실행
if __name__ == "__main__":
    # 파일명 정의
    today_str = datetime.now().strftime("%Y%m%d")
    raw_file = f"daily_sales_{today_str}.csv"
    result_file = f"summary_report_{today_str}.csv"
    
    # 프로세스 실행
    create_dummy_daily_report(raw_file) # 1. 데이터 준비
    process_report(raw_file, result_file) # 2. 처리 및 리포팅
