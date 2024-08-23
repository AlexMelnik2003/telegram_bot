import telebot
import requests
import json

bot = telebot.TeleBot('7432077431:AAHNDxeJEfYtnEAJC1BeJ8dtuucUoHypMq8')
API = 'df60cc0b74bc46a3b8c0f1b11d27ba77'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        wind = data["wind"]['speed']
        bot.reply_to(message, f'Сейчас погода: {temp}, Ветер: {wind}')


        image = 'солнце.png' if temp > 5.0 else 'тучки.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, 'Город указан не верно!')



bot.polling(none_stop=True)
