# 텔레그램 bot 기능을 활용하여 메시지 자동응답 보내는 코드 만들기
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

token=''
id=''

bot=telegram.Bot(token)
bot.sendMessage(chat_id=id,text='자동응답 테스트')

updater=Updater(token=token, use_context=True)
dispatcher=updater.dispatcher

def handler(update,context):
    user_text=update.message.text
    if user_text=='안녕':
        bot.send_message(chat_id=id,text="어 그래 안녕")
    elif user_text=='뭐해':
        bot.send_message(chat_id=id,text="그냥 있어")

echo_handler=MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)