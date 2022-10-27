import telebot.types
from telebot import TeleBot
import telebot
import random
from telebot import types

bot = TeleBot('5780919950:AAEmgkNWuGtaW38VIN-QYlAZj12mMYiKcew')

def calc(text):
    try:
        res = 0
        if "i" and "+" in text:
            lst = text.split('+')
            res = f'{float(lst[0])} + {float(lst[1])}'
        if "+" in text:
            lst = text.split('+')
            res = float(lst[0])+float(lst[1])
            return res
        elif "-" in text:
            lst = text.split('-')
            res = float(lst[0])-float(lst[1])
            return res
        elif "*" in text:
            lst = text.split('*')
            res = float(lst[0])*float(lst[1])
            return res
        elif "/" in text:
            lst = text.split('/')
            res = float(lst[0])/float(lst[1])
            return res
        else:
            res = 'Вы ввели не то, введите два числа и между ними действие, например: 2*3'
            return res
    except:
        res = 'Я не понимаю запятых, поменяйте пожалуйста  на точки, и могу решать одно действие'
        return res


@bot.message_handler(commands=["start"])
def start(m, res=False):
        # Добавляем две кнопки
        # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        # item1 = types.KeyboardButton("Рациональные")
        # item2 = types.KeyboardButton("Комплексные")
        # markup.add(item1)
        # markup.add(item2)
        bot.send_message(m.chat.id, 'Привет,я работаю калькулятором, введи два числа и '
                                    'между ними знак действия(*,-,+,/) например: 2*3')

# @bot.message_handler()
# def echo(msg: telebot.types.Message):
#     bot.send_message(msg.from_user.id, 'Привет, я работаю калькулятором, но могу только делать одно действие '
#                                        'поэтому введи два числа и между ними действие, например 23*25.6' )
#     bot.send_message(chat_id=msg.from_user.id, text=f'Результат: {calc(msg.text)}')


@bot.message_handler(content_types=["text"])
def what_do(msg):
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат: {calc(msg.text)}')


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Рациональные':
        bot.send_message(message.chat.id, "Введите два числа и между ними действие, например: 23*25.6")
    elif message.text.strip() == 'Комплексные':
        bot.send_message(message.chat.id, "Введите два числа (второе с i) и между ними действие, например: 23*25i")

bot.polling(none_stop=True)

