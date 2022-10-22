import csv


def find_login():
    name = input("Введите вашу фамилию, имя, отчество через запятую: ")
    count = 0
    with open("administrators.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь администратором")
                name = 1
                return name
    with open("teachers.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь учителем")
                name = 2
                return name
    with open("pupils.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь учеником")
                name = 3
                return name
    if name == 4:
        count += 1
    else:
        print("Вы ввели с ошибкой или не зарегистрированы в системе, обратитесь к администратору")

find_login()