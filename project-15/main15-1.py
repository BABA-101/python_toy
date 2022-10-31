# Slack으로 스마트폰에 메시지 보내기
# 사전 준비
# 1. 워크스페이스 생성
# 2. 봇 만들기 위해 https://api.slack.com 사이트 접속
# 3. Create an app > From scratch > 봇 이름 설정 및 워크스페이스 설정 
# 4. 봇 설정에서 Incoming Webhooks 탭 > On
# 5. Add New Webhooks to Workspace
# 6. 채널 선택 후 허용
# 7. Webhook URL 주소 Copy해두기
# 8. Slack 워크스페이스 확인해보면 앱 항목에 봇 생성되어있음 확인
import requests
import json

slack_webhook_url=""

def sendSlackWebhook(strText):
    headers={
        "Content-type":"application/json"
    }

    data = {
        "text": strText
    }

    res=requests.post(slack_webhook_url,headers=headers, data=json.dumps(data))

    if res.status_code == 200:
        return "ok"
    else:
        return "error"

print(sendSlackWebhook("안녕하세요 파이썬에서 보내는 메시지입니다."))

# 개인적으로 추가해봄
while True:
    text1 = input('전송할 메시지 입력 > ')
    sendSlackWebhook(text1)
    if text1=="exit()":
        break
