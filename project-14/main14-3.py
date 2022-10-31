from fileinput import filename
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

send_email = "googleEmail"
send_pwd="googleAPPpwd"

recv_email = "recvEmail"

smtp_name="smtp.gmail.com"
smtp_port=587

# 메세지 형식을 복합으로 선언하여 첨부파일을 보낼 수 있도록 함.
msg = MIMEMultipart()

msg['Subject']="첨부파일 테스트 입니다."
msg['From']=send_email
msg['To']=recv_email

text = """
첨부파일 메일 테스트 내용
감사링
"""

contentPart=MIMEText(text)
msg.attach(contentPart)

etc_file_path=r'project-14\첨부파일.txt'
with open(etc_file_path,'rb') as f:
    etc_part =MIMEApplication(f.read())
    etc_part.add_header('Content-Disposition','attachment',filename="첨부파일.txt")
    msg.attach(etc_part)

s=smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()
