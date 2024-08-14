import telebot
import webbrowser

bot = telebot.TeleBot('7432077431:AAHNDxeJEfYtnEAJC1BeJ8dtuucUoHypMq8')


@bot.message_handler(commands=['web', 'website'])
def site(message):
    webbrowser.open('https://www.youtube.com')


@bot.message_handler(commands=['start', 'hello'])
def main(message):
    bot.send_message(message.chat.id, f'Hello! {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Hello! {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
