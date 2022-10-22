
import show_cshedule as sh

data = "schedule.csv"
data_hw = "homework.csv"
data_mark = "marks.csv"


def menu_pupil():
    task = 0
    while task < 4:
        try:
            task = int(input("Привет, выбери пункт меню: \n"
                         "1 - Посмотреть расписание \n"
                         "2 - Посмотреть домашнюю работу \n"
                         "3 - Посмотреть текущие оценки \n"
                         "4 - Выход \n"
                         "Введи нужную цифру \n"))

            if task == 1:
                sh.read(data)
            elif task == 2:
                sh.read(data_hw)
            elif task == 3:
                sh.read(data_mark)
            elif task == 4:
                break

        except:
            print("НЕ то ввели, попробуйте еще раз")
        print("Вы вышли из программы, запустите еще раз")


menu_pupil()
