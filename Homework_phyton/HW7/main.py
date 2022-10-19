import first
import view

a = -1
while a == -1:
    print("Выберите пункт меню: "
          "1)Чтение "
          "2)Запись "
          "3)Импорт "
          "4)Экспорт "
          "5)Выход ")
    b = int(input("Введите пункт меню числом от 1 до 5 "))
    if b == 2:
        first.add_man()
    elif b == 1:
        first.read_file()

