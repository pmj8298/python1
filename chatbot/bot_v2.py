from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import talk_pmj as tk
import gemini
from dotenv import load_dotenv
import os

#.env 파일 로드
load_dotenv()

TOKEN = os.getenv('TTOKEN')

# TOKEN = '71733108316538:AAETkO83Pry573XGynngAUVC6XT86qxc0jQ'

# TRIGGER_WORDS = {
#     '안녕':'안녕하세요! 반가워용😊',
#     '정보':'어떤 정보가 필요하세요?🤔',
#     '기분':'오늘 기분이 좋아요😍'
# }

async def start(update, context):
    await update.message.reply_text('안녕! 무엇을 도와드릴까요?')

async def send_photo(update, context):
    # photo_url = 'https://i.namu.wiki/i/R0AhIJhNi8fkU2Al72pglkrT8QenAaCJd1as-d_iY6MC8nub1iI5VzIqzJlLa-1uzZm--TkB-KHFiT-P-t7bEg.webp'
    # await update.message.reply_photo(photo = photo_url, caption = '사진이미지 전송')

    photo_path = "D:/pmj/python/image1.jpg"
    with open(photo_path, "rb") as photo:
        await update.message.reply_photo(photo=photo, caption="사진이미지 전송")


async def monitor_chat(update, context):
    user_text = update.message.text # 감지된 메시지들 ex.택배물건
    chat_id = update.message.chat_id # 메시지가 온 채팅방  ex. 택배 배송지

    if 'gpt' in user_text:
        res = gemini.aiai(user_text.replace('gpt',''))
        await context.bot.send_message(chat_id = chat_id, text = res) #, parse_mode='MarkdownV2'
    elif '영화정보' in user_text: pass
        #await 영화정보크롤링()함수를 실행
    elif '사진줘' in user_text:
        await send_photo(update, context)
    else:
        for key, res in tk.TRIGGER_WORDS.items():
            if key in user_text:
                await context.bot.send_message(chat_id = chat_id, text = res)
                break #한개의 키워드에만 반응


def main():
    app = Application.builder().token(TOKEN).build()

    # 명령어 핸들러 추가
    app.add_handler(CommandHandler('start',start))

    # 응답 핸들러 추가
    # ~은 TEXT는 하되, COMMAND는 하지마라
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, monitor_chat))

    print('봇이 실행중입니다. 모니터링 중...')
    app.run_polling()




if __name__=='__main__':
   main()


