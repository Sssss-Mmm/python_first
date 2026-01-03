"""
OS Automation Basics Example
----------------------------
이 파일은 RPA의 기초가 되는 운영체제(OS) 및 파일 시스템 제어 기능을 다룹니다.
1. File Organization: 파일을 확장자별로 자동 분류하여 폴더 이동.
2. Archiving: 특정 폴더를 자동으로 압축(Zip).
3. Path Handling: 경로 조작 및 안전한 파일 제어.
"""

import os
import shutil
import zipfile
from datetime import datetime

def setup_dummy_files(base_dir):
    """테스트를 위한 임시 파일 생성"""
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # 생성할 가상 파일들
    files = [
        "report_2025.txt", "data_2025.csv", "image.png", 
        "summary.xlsx", "notes.txt", "backup.zip"
    ]
    
    print(f"[Setup] '{base_dir}' 폴더에 테스트 파일 생성 중...")
    for f in files:
        with open(os.path.join(base_dir, f), 'w') as file:
            file.write(f"This is a dummy content for {f}")

def organize_files_by_extension(source_dir):
    """파일 확장자별로 폴더를 생성하여 이동"""
    print(f"\n[Step 1] '{source_dir}' 내의 파일 정리 시작...")
    
    items = os.listdir(source_dir)
    
    for item in items:
        item_path = os.path.join(source_dir, item)
        
        # 파일인 경우에만 처리 (폴더 제외)
        if os.path.isfile(item_path):
            # 확장자 추출 (e.g., .txt)
            _, ext = os.path.splitext(item)
            ext = ext.lower().replace('.', '') # 점 제거 및 소문자화
            
            if not ext: # 확장자가 없는 경우
                ext = "others"
                
            # 확장자별 폴더 경로
            target_folder = os.path.join(source_dir, ext)
            
            # 폴더가 없으면 생성
            if not os.path.exists(target_folder):
                os.makedirs(target_folder)
            
            # 파일 이동
            shutil.move(item_path, os.path.join(target_folder, item))
            print(f"  Move: {item} -> {ext}/{item}")

def create_zip_archive(source_dir, output_filename):
    """폴더 전체를 압축"""
    print(f"\n[Step 2] '{source_dir}' 폴더를 '{output_filename}'으로 압축 중...")
    
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # os.walk로 하위 폴더까지 모두 탐색
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                # 압축 파일 내부의 경로 이름 설정 (절대 경로가 아닌 상대 경로로)
                arcname = os.path.relpath(file_path, start=os.path.dirname(source_dir))
                zipf.write(file_path, arcname)
                
    print(f"  Complete: {output_filename} 생성 완료 ({os.path.getsize(output_filename)} bytes)")

def run_os_automation_examples():
    # 테스트용 기본 경로
    base_dir = "temp_automation_test"
    
    # 1. 테스트 환경 세팅
    setup_dummy_files(base_dir)
    
    # 2. 파일 정리 실행
    organize_files_by_extension(base_dir)
    
    # 3. 정리된 폴더 압축
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_name = f"backup_{timestamp}.zip"
    create_zip_archive(base_dir, zip_name)
    
    # 4. 청소 (테스트 후 삭제)
    # print("\n[Cleanup] 테스트 폴더 및 파일 삭제...")
    # shutil.rmtree(base_dir)
    # os.remove(zip_name)
    print("\n* 테스트 완료. 생성된 'temp_automation_test' 폴더와 zip 파일을 확인해보세요.")

if __name__ == "__main__":
    run_os_automation_examples()
