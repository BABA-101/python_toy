# 텔레그램으로 스마트폰에 메시지 보내기
# API 토큰 이용하여 bot id 알아내기
import telegram

token = ''
bot = telegram.Bot(token=token)
updates=bot.getUpdates()
for u in updates:
    print(u.message)