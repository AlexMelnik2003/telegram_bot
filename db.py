import telebot
import sqlite3

bot = telebot.TeleBot('7432077431:AAHNDxeJEfYtnEAJC1BeJ8dtuucUoHypMq8')

@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, сейчас тебя зарегистрирую! Введи своё имя')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введи пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()