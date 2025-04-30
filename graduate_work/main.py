import telebot
import telebot.types
from config import BOT_TOKEN, API_KEY


bot = telebot.TeleBot(BOT_TOKEN) 


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, вонючка!')


if __name__ == '__main__':
    bot.infinity_polling()

a = 3
b = 6

if a == b:
    print(True)
