# 네이버 이메일을 읽어보는 코드 

import imaplib
import email
from email import policy

# 문자열을 인코딩하는 함수
def find_encoding_info(txt):
    info = email.header.decode_header(txt)
    subject, encode = info[0]
    return subject,encode

imap=imaplib.IMAP4_SSL('imap.gmail.com')
id=""
pw="" #구글은 앱비번
imap.login(id,pw)

# 받은 메일함에서 메일을 읽는다.
imap.select('INBOX')
resp,data = imap.uid('search',None,'All')
all_email=data[0].split()
last_email=all_email[-5:]

# 최신 메일부터 출력하여 반복. reversed()로 리스트 뒤집어서 최신 메일부터 출력
for mail in reversed(last_email):
    result, data = imap.uid('fetch',mail,'(RFC822)')
    raw_email=data[0][1]
    email_message=email.message_from_bytes(raw_email,policy=policy.default)

    print('='*70)
    print('FROM: ',email_message['From'])
    print('Sender: ',email_message['Sender'])
    print('To: ',email_message['To'])
    print('Date: ',email_message['Date'])
    subject, encode = find_encoding_info(email_message['subject'])
    print('SUBJECT: ',subject)
    print('='*70)

imap.close()
imap.logout()