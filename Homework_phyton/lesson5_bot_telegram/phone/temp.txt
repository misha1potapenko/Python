
from telebot import TeleBot
import telebot
from telebot import types


bot = TeleBot('')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("/show")
    btn2 = types.KeyboardButton('/add_contact')
    btn3 = types.KeyboardButton("/export_columns")
    btn4 = types.KeyboardButton("/export_lines")
    btn5 = types.KeyboardButton("/find")
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот и являюсь телефонной книгой, "
                                           "выбери что надо сделать /show  /export_columns  "
                                           " /export_lines  или /find "
                                           "ещё я могу дописать в телефонную книгу если скинешь мне файл".format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['show'])
def hello(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id,
                     text='Это телефонная книга, можешь ее открыть и посмотреть')
    bot.send_document(chat_id=msg.from_user.id, document=open('phone_book.txt', 'rb'))


@bot.message_handler(commands=['export_columns'])
def exp_c(msg: telebot.types.Message):
    with open('phone_book.txt', encoding='utf-8') as f:
        lines = f.readlines()

    with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
        for each in lines:
            if each.__contains__(','):
                str = each.split(', ')
                g.writelines('\n'.join(str))
                g.writelines('\n')
    bot.send_message(chat_id=msg.from_user.id,
                     text='Phone book \n')
    bot.send_document(chat_id=msg.from_user.id, document=open('phone_book_exp.txt', 'rb'))


@bot.message_handler(commands=['export_lines'])
def exp_l(msg: telebot.types.Message):
    with open('phone_book.txt', "r", encoding='utf-8') as f:
        with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
            for line in f:
                g.write(line)
    bot.send_message(chat_id=msg.from_user.id,
                     text='Phone book \n')
    bot.send_document(chat_id=msg.from_user.id, document=open('phone_book_exp.txt', 'rb'))

@bot.message_handler(content_types=['document'])
def hello(msg: telebot.types.Message):
    file = bot.get_file(msg.document.file_id)
    downloaded_file = bot.download_file(file.file_path)
    msg.document.file_name = 'temp.txt'
    with open('temp.txt', 'wb') as f_out:
        f_out.write(downloaded_file)
    with open('temp.txt', "r", encoding='utf-8') as f, open('phone_book.txt', "a", encoding='utf-8') as g:
        g.writelines('\n')
        for line in f:
            if len(line) > 20:
                g.writelines(line)
                g.writelines('\n')
        if len(line) < 20:
            with open('temp.txt', encoding='utf-8') as k:
                lines = k.readlines()
            with open('phone_book.txt', "a", encoding='utf-8') as l:
                j = 0
                lst1 = []
                for each in lines:
                    if not each.__contains__(','):
                        if each != '\n':
                            lst1.append(each.replace("\n", ""))
                            j += 1
                            if j == 4:
                                l.writelines(', '.join(lst1))
                                l.writelines('\n')
                                j = 0
                                lst1 = []

def searching(text):
    search_value = text

    with open('phone_book.txt','r', encoding='utf-8') as file:
        count = 0
        for line in file:
            if search_value in line:
                return line
        if count == 0:
            return 'не найдено'


@bot.message_handler(commands=['find'])
def search_data(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text= "Введите данные для поиска:")
    bot.register_next_step_handler(callback=sum_items, message=msg)


def sum_items(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=searching(msg.text))



@bot.message_handler(commands=['add_contact'])
def add_contact(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Добавьте ФИО и номер телефона")
    bot.register_next_step_handler(callback=add_cont, message=msg)


def add_cont(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text=add_con(msg.text))


def add_con(text):
    doc = open('phone_book.txt', 'a', encoding='utf-8')
    doc.write("\n{imia}".format(imia=text))
    return "Добавлено"

@bot.message_handler()
def echo(msg: telebot.types.Message):
    bot.send_message(msg.from_user.id, "Ивините, я Вас не понял, введите команду /start" )



bot.polling(none_stop=True)

