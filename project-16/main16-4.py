# 이메일로 특정 키워드가 오면 스마트폰으로 알림보내기
# slack으로 보낸다.  (반복version)
import email
import imaplib
from email import policy
import requests
import json
import time

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

send_list=[]

while True:
    try:
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
                # send_list에 메시지가 없다면 조건에 만족. 즉, 새로운 메시지가 있으면 조건에 만족한다.
                if slack_send_message not in send_list:
                    sendSlackWebhook(slack_send_message)
                    print(slack_send_message)
                    # send_list에 보낸 메시지 추가, append 통해 리스트 마지막에 원소 추가.
                    send_list.append(slack_send_message)
        time.sleep(30)
    #키보드 인터럽트 발생 시 while문 종료
    except KeyboardInterrupt:
        break
imap.close()
imap.logout()