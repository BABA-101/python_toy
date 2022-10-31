# 이메일로 특정 키워드가 오면 스마트폰으로 알림보내기
# slack으로 보낸다. 
import email
import imaplib
from email import policy
import requests
import json

slack_webhook_url=""

def sendSlackWebhook(strText):
    headers={
        "Content-type":"application/json"
    }

    data={
        "text":strText
    }

    res=requests.post(slack_webhook_url, headers=headers,data=json.dumps(data))
    if res.status_code ==200:
        return "ok"
    else:
        return "error"

def find_encoding_info(txt):
    info=email.header.decode_header(txt)
    subject, encode = info[0]
    return subject,encode

imap=imaplib.IMAP4_SSL('imap.gmail.com')
id=''
pw=''
imap.login(id,pw)

imap.select('INBOX')
resp,data=imap.uid('search',None,'All')
all_email=data[0].split()
last_email=all_email[-5:]

for mail in reversed(last_email):
    result, data = imap.uid('fetch',mail,'(RFC822)')
    raw_email=data[0][1]
    email_message=email.message_from_bytes(raw_email,policy=policy.default)

    emain_from=str(email_message['From'])
    emain_date=str(email_message['Date'])
    subject,encode = find_encoding_info(email_message['Subject'])
    subject_str=str(subject)
    if subject_str.find('KEYWORD') >= 0:
        slack_send_message=emain_from + '\n' + emain_date + '\n' + subject_str
        sendSlackWebhook(slack_send_message)
        print(slack_send_message)

imap.close()
imap.logout()