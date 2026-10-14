import telebot

BOT_TOKEN = "8650165154:AAFNmunvvhbCzhx2Yhpc_NzPUAYKWo-hKnA"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "اهلا بيك البوت شغال ✅")

bot.infinity_polling()
