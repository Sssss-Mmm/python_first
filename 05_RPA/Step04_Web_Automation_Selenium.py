"""
[Step 04] Web Automation (Selenium)
-----------------------------------
웹 사이트에 접속하여 로그인, 검색, 데이터 추출 등을 자동화합니다.
Selenium은 가장 강력한 웹 자동화 도구 중 하나입니다.

[필수 설치]
pip install selenium webdriver-manager

[주의]
이 코드는 Chrome 브라우저가 설치되어 있어야 실행됩니다.
"""

import time
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
except ImportError:
    print("[Error] 'selenium' 또는 'webdriver_manager'가 설치되지 않았습니다.")
    print("터미널에서 'pip install selenium webdriver-manager'를 실행해주세요.")
    exit()

def run_web_search_automation(keyword="Python RPA"):
    print("[Step 1] 브라우저 실행 중...")
    
    # 1. 브라우저 옵션 설정 (자동 꺼짐 방지)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True) # 스크립트가 끝나도 브라우저 유지
    # options.add_argument("--headless") # 브라우저 창을 띄우지 않으려면 주석 해제
    
    # 2. 드라이버 자동 설치 및 실행
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    try:
        # 3. 사이트 이동 (구글)
        url = "https://www.google.com"
        print(f" -> 이동: {url}")
        driver.get(url)
        time.sleep(1) # 로딩 대기
        
        # 4. 검색창 찾기 및 입력
        # 구글 검색창의 name 속성은 보통 'q' 입니다. (바뀔 수 있음)
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.RETURN) # 엔터키 입력
        
        print(f" -> 검색어 입력 및 실행: {keyword}")
        time.sleep(2) # 검색 결과 로딩 대기
        
        # 5. 검색 결과 제목 가져오기 (예시)
        # CSS Selector로 검색 결과 제목(h3)들을 찾습니다.
        results = driver.find_elements(By.CSS_SELECTOR, "h3")
        
        print(f"\n[검색 결과 상위 5개]")
        for i, result in enumerate(results[:5], 1):
            print(f"{i}. {result.text}")
            
    except Exception as e:
        print(f"[Error] 실행 중 오류 발생: {e}")
        
    finally:
        print("\n[Complete] 5초 후 브라우저를 종료합니다.")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    search_query = input("구글에서 검색할 내용을 입력하세요 (기본값: Python RPA): ") or "Python RPA"
    run_web_search_automation(search_query)
