# html 형식으로 메일 보내기
# 텍스트가 아닌 html. 메일의 내용을 꾸며서 전송 가능
# https://html5-editor.net/
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email=""
send_pwd=""

recv_email=""

smtp_name="smtp.gmail.com"
smtp_port=587

msg = MIMEMultipart()

msg['Subject']="html로 보내는 메일 입니다."
msg['From']=send_email
msg['To']=recv_email

html_body="""
<h2>안녕하세요. 파이싼 자동화 테스트. html 형식으로 보내는 이메일 테스트이다.</h2>
<p><span style="color: #0000ff;">글자 색상 지정 간으!</span></p>
<h3>크기 조정 가능!</h3>
<p>표도 만들 수 있다.</p>
<table style="width: 190px;">
<tbody>
<tr>
<td style="width: 52.2125px;">1</td>
<td style="width: 63.7875px;">2</td>
<td style="width: 78px;">3</td>
</tr>
<tr>
<td style="width: 52.2125px;">표를</td>
<td style="width: 63.7875px;">만들 수</td>
<td style="width: 78px;">있다</td>
</tr>
<tr>
<td style="width: 52.2125px;">4</td>
<td style="width: 63.7875px;">5</td>
<td style="width: 78px;">6</td>
</tr>
</tbody>
</table>

"""
msg.attach(MIMEText(html_body,'html'))
s=smtplib.SMTP(smtp_name,smtp_port)
s.starttls()
s.login(send_email,send_pwd)
s.sendmail(send_email,recv_email,msg.as_string())
s.quit()