import telepot
import time
from newspesabot.config import Config
from newspesabot.data_handler import *

client = Config.connect_to_mongo()


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    content = msg["text"]
    collection = client["spesabot"]["lista"]
    if content_type == 'text':
        DataHandler.insert_element(chat_id, content, collection)
        bot.sendMessage(chat_id, 'Ho inserito' + content)


TOKEN = Config.token

bot = telepot.Bot(TOKEN)
bot.message_loop(on_chat_message)

print('Listening ...')


def main():
    while 1:
        time.sleep(10)
