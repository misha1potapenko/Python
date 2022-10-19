#добавление записи в файл


def add_new_data(data, data_colum):
    print('Если вы хотите добавить запись в строку - выберите 1, если в столбик - 2')
    user_choice = int(input())
    if user_choice == 2:
        with open(data_colum, 'a', encoding='utf-8') as f:
            f.writelines('\n' + input('Введите фамилию \n'))
            f.writelines('\n' + input('Введите Имя \n'))
            f.writelines('\n' + input('Введите номер телефона \n'))
            f.writelines('\n' + input('Введите комментарий \n') )
            f.writelines('\n ')
    elif user_choice == 1:
        with open(data, 'a', encoding='utf-8') as f:
            f.writelines('\n' + input('Введите данные через запятую \n'))
            f.write(';')
    else:
        print("Выбор некорректен, Вы вышли в главное меню ")