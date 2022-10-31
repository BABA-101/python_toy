import smtplib
from email.mime.text import MIMEText

send_email="송신자메일"
send_pwd="패스워드"

recv_email="수신자메일"

# 구글 메일의 smtp 주소
smtp_name="smtp.gmail.com"
smtp_port=587

text="""
테스트 메일
"""
msg=MIMEText(text)

msg['Subject']="메일 제목"
msg['From']=send_email
msg['To']=recv_email
print(msg.as_string())

s=smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email,recv_email,msg.as_string)
s.quit()