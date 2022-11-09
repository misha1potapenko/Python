
from telebot import TeleBot
import telebot
from telebot import types
from time import time

bot = TeleBot('')


def my_log(msg: telebot.types.Message):
    with open('logfile.log', 'a', encoding='UTF-8') as n_log:
        print(time(), f'Пользователь ({msg.from_user.id}) прислал сообщение: {msg.text}', file=n_log)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    with open('logfile.log', 'a', encoding='UTF-8') as n_log:
        print(time(), 'Бот запущен', file=n_log)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/ration")
    btn2 = types.KeyboardButton("/comprehensive")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот и могу работать калькулятором, "
                                           "выбери с какими числами работать /ration или /comprehensive".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['export'])
def exp_l(msg: telebot.types.Message):
    with open('logfile.log', "r", encoding='utf-8') as f:
        bot.send_document(chat_id=msg.from_user.id, document=open('logfile.log', 'rb'))


@bot.message_handler(commands=["ration"])
def handle_text(msg: telebot.types.Message):
    my_log(msg)
    bot.send_message(msg.chat.id, text="Введите несколько чисел и между ними действие, например: 23*25.6-5+7")
    bot.register_next_step_handler(callback=viev_calc, message=msg)


def viev_calc(msg: telebot.types.Message):
    my_log(msg)
    bot.send_message(chat_id=msg.from_user.id, text=calc(msg.text))


OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
             '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y)}


def calc(formula):
    try:
        def parse(formula_string):
            number = ''
            for s in formula_string:
                if s in '1234567890.':
                    number += s
                elif number:
                    yield float(number)
                    number = ''
                if s in OPERATORS or s in "()":
                    yield s
            if number:
                yield float(number)

        def shunting_yard(parsed_formula):
            stack = []
            for token in parsed_formula:
                if token in OPERATORS:
                    while stack and stack[-1] != "(" and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]:
                        yield stack.pop()
                    stack.append(token)
                elif token == ")":
                    while stack:
                        x = stack.pop()
                        if x == "(":
                            break
                        yield x
                elif token == "(":
                    stack.append(token)
                else:
                    yield token
            while stack:
                yield stack.pop()

        def calc(polish):
            stack = []
            for token in polish:
                if token in OPERATORS:
                    y, x = stack.pop(), stack.pop()
                    stack.append(OPERATORS[token][1](x, y))
                else:
                    stack.append(token)
            return stack[0]

        return calc(shunting_yard(parse(formula)))

    except:
        res = 'Ввод не корректен, введите  числа в стоку с действиями' \
              ' между ними без пробелов, например 22*3/5-4+6'
        return res

@bot.message_handler(commands=["comprehensive"])
def handle_text(msg: telebot.types.Message):
        my_log(msg)
        bot.send_message(msg.chat.id, text="Введите два комплексных числа и между ними действие,"
                                           " например: 23+25j - 6-24j (с пробелами между действием)")
        bot.register_next_step_handler(callback=viev_calc2, message=msg)


def viev_calc2(msg: telebot.types.Message):
    my_log(msg)
    bot.send_message(chat_id=msg.from_user.id,  text=compreh(msg.text))


def compreh(text):
    try:
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
    except:
        res = 'Ввод не корректен'
        return res
@bot.message_handler()
def echo(msg: telebot.types.Message):
    my_log(msg)
    bot.send_message(msg.from_user.id, "Ивините, я понимаю только команды /ration и /comprehensive" )

@bot.message_handler(commands=['export'])
def exp_l(msg: telebot.types.Message):
    with open('logfile.log', "r", encoding='utf-8') as f:
        bot.send_document(chat_id=msg.from_user.id, document=open('logfile.log', 'rb'))

bot.polling(none_stop=True)
