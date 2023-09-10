import telebot

from telebot import TeleBot

bot: TeleBot = telebot.TeleBot('TOKEN')


@bot.message_handler()
def msg(message):
    bot.send_message(message.chat.id, message.text)


bot.infinity_polling()