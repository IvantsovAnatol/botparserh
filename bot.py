import telebot

token = ''
id_chanel = "@parserssssq_bot"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def commands(message):
    bot.send_message(id_chanel, message.text)



bot.polling()
