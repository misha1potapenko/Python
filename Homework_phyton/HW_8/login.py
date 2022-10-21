import csv


def find_login():
    name = input("Введите вашу фамилию, имя, отчество через запятую: ")
    with open("administrators.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь администратором")
                name = 1
    with open("teachers.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь учителем")
                name = 1
    with open("pupils.csv", "r", encoding="UTF-8") as f:
        for line in f:
            if name in line:
                print("Вы являетесь учеником")
                name = 1
    if name == 1:
        name = True
    else:
        print("Вы ввели с ошибкой или не зарегистрированы в системе, обратитесь к администратору")

find_login()