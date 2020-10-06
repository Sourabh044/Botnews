import os
from flask import Flask , request

import telebot



TOKEN = "1244507332:AAHNRaWB4kdRTyEKpeFklpoMtjvR2K_xPyY"

bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello, How are you!\nI will provide u latest news on Tech \n made by @demonic_bunny")

@bot.message_handler(commands=['news'])
def send_welcome(message):
    bot.reply_to(message, "Hello, How are you!\nI will provide u latest news on Tech \n made by @demonic_bunny")

server.route('/' + TOKEN, methods=['POST'])
def getMessage():\
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=)
    return "!", 200
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))