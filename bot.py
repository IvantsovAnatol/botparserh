import telebot

token = '8545268244:AAGyfMZJwRQHHtB7GrS2c6jWlcw41Nj754U'
id_chanel = "@parserssssq_bot"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def commands(message):
    bot.send_message(id_chanel, message.text)



bot.polling()