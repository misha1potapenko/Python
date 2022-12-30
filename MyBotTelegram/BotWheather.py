
from telebot import TeleBot

from telebot import types


bot = TeleBot('5970116250:AAGNdG-tEUTcvP6fydewOP28-dpC2K8N8gM')




# @bot.message_handler(commands=['start', 'help'])
# def start(message):
#     with open('logfile.log', 'a', encoding='UTF-8') as n_log:
#         print(time(), 'Бот запущен', file=n_log)
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton("/ration")
#     btn2 = types.KeyboardButton("/comprehensive")
#     markup.add(btn1, btn2)
#     bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот и могу работать калькулятором, "
#                                            "выбери с какими числами работать /ration или /comprehensive".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Прогноз погоды Воронеж", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=51.65&lon=39.20&lang=en&type=graph&units=m&run=12')
    markup.add(button1)
    button2 = types.InlineKeyboardButton("Прогноз погоды Борисоглебск", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=51.36&lon=42.09&lang=en&type=graph&units=m&run=12')
    markup.add(button2)
    button3 = types.InlineKeyboardButton("Прогноз погоды Балашов", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=51.54&lon=43.18&lang=en&type=graph&units=m&run=12')
    markup.add(button3)
    button4 = types.InlineKeyboardButton("Прогноз погоды Сокол", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=51.58&lon=45.84&lang=en&type=graph&units=m&run=12')
    markup.add(button4)
    button5 = types.InlineKeyboardButton("Прогноз погоды Сызрань", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=53.23&lon=48.54&lang=en&type=graph&units=m&run=12')
    markup.add(button5)
    button6 = types.InlineKeyboardButton("Прогноз погоды Пугачев", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=52.02&lon=48.81&lang=en&type=graph&units=m&run=12')
    markup.add(button6)
    button7 = types.InlineKeyboardButton("Прогноз погоды Шагол", url='https://www.meteopt.com/modelos/meteogramas/gfs.php?lat=55.17&lon=61.51&lang=en&type=graph&units=m&run=12')
    markup.add(button7)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт)".format(message.from_user), reply_markup=markup)


bot.polling(none_stop=True)


