@bot.message_handler(commands=['summator'])
def help_command(msg: telebot.types.Message):
    bot.send_message(chat_id=msg.from_user.id, text="Введите числа через пробел")
    bot.register_next_step_handler(callback=sum_items, message=msg)