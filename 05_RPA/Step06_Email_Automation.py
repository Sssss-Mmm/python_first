"""
[Step 06] Email Automation (smtplib)
------------------------------------
Python의 기본 내장 라이브러리인 'smtplib'를 사용하여 이메일을 자동으로 발송합니다.
첨부파일(엑셀 등)을 같이 보낼 때 유용합니다.

[주의]
이 코드는 실제 메일 서버와 계정 정보가 필요합니다.
Google Gmail 등을 사용할 경우 '앱 비밀번호' 설정이 필요할 수 있습니다.
여기서는 보안상 실제 전송하지 않고 로직만 설명합니다.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

def send_email_simulation(sender_email, receiver_email, password):
    print(f"[Step 1] 이메일 발송 준비: {sender_email} -> {receiver_email}")
    
    # 1. 메일 객체 생성
    msg = MIMEMultipart()
    msg['Subject'] = "[RPA] 일일 업무 자동 보고"
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # 2. 본문 추가
    text = """
    안녕하세요.
    Python RPA 스크립트가 자동으로 보낸 메일입니다.
    첨부된 엑셀 파일을 확인해주세요.
    감사합니다.
    """
    msg.attach(MIMEText(text))
    
    # 3. 파일 첨부 (앞서 만든 엑셀 파일이 있다면 첨부)
    filename = "sales_report_rpa.xlsx"
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            attachment = MIMEApplication(f.read())
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(attachment)
            print(f" -> 첨부파일 추가됨: {filename}")
    else:
        print(f" -> 경고: 첨부할 파일 '{filename}'이 없어 스킵합니다.")
            
    # 4. 서버 연결 및 전송 (시뮬레이션)
    print("\n[Step 2] SMTP 서버 연결 시도...")
    
    # ------------------------------------------------------------------
    # 실제 사용 시 아래 주석을 해제하고 서버 정보를 입력해야 합니다.
    # ------------------------------------------------------------------
    try:
        # with smtplib.SMTP('smtp.gmail.com', 587) as server:
        #     server.starttls() # 보안 연결
        #     server.login(sender_email, password) # 로그인
        #     server.send_message(msg)
        #     print(" -> 전송 완료!")
        
        print("[Simulation Mode] 실제 전송 대신 로그만 출력합니다.")
        print(f" -> Sending Message ID: {msg['Subject']}")
        print(" -> 전송 성공 (가정)")
        
    except Exception as e:
        print(f" -> 전송 실패: {e}")

if __name__ == "__main__":
    # 테스트 계정 정보 (가짜)
    my_email = "my_email@example.com"
    my_password = "my_password_1234"
    target_email = "manager@example.com"
    
    # 엑셀 파일이 없으면 하나 만들고 시작 (테스트용)
    if not os.path.exists("sales_report_rpa.xlsx"):
        print("* 테스트를 위해 빈 파일 생성 중...")
        with open("sales_report_rpa.xlsx", "w") as f:
            f.write("dummy data")
            
    send_email_simulation(my_email, target_email, my_password)
