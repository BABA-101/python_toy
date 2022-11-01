# 텔레그램 bot으로 메시지 전송하기
import telegram

token=''
id=''

bot=telegram.Bot(token)
bot.sendMessage(chat_id=id,text="파이썬으로 보내는 메시지")

while True:
    text1=input('전송할 메시지 >> ')
    bot.sendMessage(chat_id=id,text=text1)
    if text1=='exit()':
        break