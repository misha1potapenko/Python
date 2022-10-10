import random
sweet = 2021

while sweet >= 28:
    try:
        user_one = int(input("1 Игрок. Ввведите число меньше или равно 28: "))
        if user_one > 28:
            user_one = int(input("Не то число, введите < 28: "))
        sweet -= user_one
        print("Осталось", sweet)
        if sweet <= 28:
            print("Победил компьютер")
            break
    except:
        print("Вы ввели ерунду, ваш ход передан другому игроку")
    user_two = random.randint(1, 28)
    print("Компьютер ввел число: ", user_two)
    sweet -= user_two
    print("Осталось", sweet)
    if sweet <= 28:
        print("Победил первый игрок")
        break


