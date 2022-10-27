
from telebot import TeleBot
import telebot
from telebot import types

bot = TeleBot('5740754370:AAFK4xn53nVw4kFXBM_WApBRtG6gtlzsc70')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/ration")
    btn2 = types.KeyboardButton("/comprehensive")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот и могу работать калькулятором, "
                                           "выбери с какими числами работать /ration или /comprehensive".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=["ration"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Введите два числа и между ними действие, например: 23*25.6")
        bot.register_next_step_handler(callback=viev_calc, message=msg)


def viev_calc(msg: telebot.types.Message):
        bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))



def calc(text):
    try:
        res = 0
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
            res = 'Вы ввели некорректно, введите два числа и между ними действие, например: 2*3'
            return res
    except:
        res = 'Я не понимаю запятых, поменяйте пожалуйста  на точки, и могу выполнять одно действие'
        return res


@bot.message_handler(commands=["comprehensive"])
def handle_text(msg: telebot.types.Message):
        bot.send_message(msg.chat.id, text="Введите два комплексных числа и между ними действие,"
                                           " например: 23+25j - 6-24j (с пробелами между действием)")
        bot.register_next_step_handler(callback=viev_calc2, message=msg)


def viev_calc2(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,  text=compreh(msg.text))


def compreh(text):
    res = None
    lst = text.split()
    if lst[1] == '-':
        res = complex(lst[0]) - complex(lst[2])
        return str(res)
    elif lst[1] == '+':
        res = complex(lst[0]) + complex(lst[2])
        return str(res)
    elif lst[1] == '/':
        res = complex(lst[0]) / complex(lst[2])
        return str(res)
    elif lst[1] == '*':
        res = complex(lst[0]) * complex(lst[2])
        return str(res)
    else:
        print('Ввод не корректен')
@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(msg.from_user.id, 'Привет, я работаю калькулятором, но могу только делать одно действие '
                                       'поэтому введи два числа и между ними действие, например 23*25.6' )
    bot.send_message(chat_id=msg.from_user.id, text=f'Результат: {calc(msg.text)}')


bot.polling(none_stop=True)

