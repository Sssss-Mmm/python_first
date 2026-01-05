"""
[Step 05] Mouse & Keyboard Automation (PyAutoGUI)
-------------------------------------------------
마우스와 키보드를 직접 제어하여, 화면상의 이미지를 인식하거나 
단축키를 입력하는 등 사람의 손을 흉내냅니다.

[필수 설치]
pip install pyautogui

[비상 정지]
PyAutoGUI는 실행 중에 마우스 제어권을 가져갑니다.
만약 동작을 멈추고 싶다면 마우스를 모니터의 4개 코너(주로 왼쪽 상단) 중 
한 곳으로 끝까지 밀어버리세요. (Fail-Safe 기능 발동)
"""

import time
try:
    import pyautogui
except ImportError:
    print("[Error] 'pyautogui' 라이브러리가 설치되지 않았습니다.")
    print("터미널에서 'pip install pyautogui'를 실행해주세요.")
    exit()

def mouse_and_keyboard_demo():
    print("[Alert] 3초 뒤에 마우스와 키보드 제어가 시작됩니다.")
    print("움직임을 멈추려면 마우스를 화면 왼쪽 위 모서리로 끝까지 미세요.")
    
    for i in range(3, 0, -1):
        print(f"{i}...")
        time.sleep(1)
        
    # 1. 화면 크기 확인
    screen_width, screen_height = pyautogui.size()
    print(f"화면 크기: {screen_width} x {screen_height}")
    
    # 2. 마우스 이동 (화면 중앙으로 1초 동안 이동)
    print(" -> 마우스 중앙 이동")
    pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=1)
    
    # 3. 마우스 클릭 (현재 위치에서 클릭)
    # pyautogui.click() 
    
    # 4. 메모장 실행 (Windows 기준 win+r -> notepad -> enter)
    # 만약 Mac/Linux라면 단축키가 다를 수 있습니다.
    print(" -> 메모장 실행 시도")
    pyautogui.hotkey('win', 'r') # 실행창 열기
    time.sleep(0.5)
    pyautogui.typewrite('notepad') # 'notepad' 입력
    time.sleep(0.5)
    pyautogui.press('enter') # 엔터키 입력
    
    time.sleep(1) # 메모장 뜰 때까지 대기
    
    # 5. 글자 입력
    print(" -> 글자 입력")
    # 한글은 pyautogui로 직접 입력이 어려울 수 있습니다. (pyperclip과 조합 필요)
    # 여기서는 영문 입력만 테스트합니다.
    pyautogui.typewrite("Hello, RPA World!", interval=0.1) 
    pyautogui.press('enter')
    pyautogui.typewrite("This is automated typing.", interval=0.1)
    
    # 6. 스크린샷 찍기
    print(" -> 스크린샷 저장")
    pyautogui.screenshot("my_screenshot.png")
    
    print("\n[Complete] 모든 동작이 완료되었습니다.")

if __name__ == "__main__":
    mouse_and_keyboard_demo()
