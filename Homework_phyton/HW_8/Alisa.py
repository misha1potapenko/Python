# Creates a dict from list
data = 'algebra.txt'


def convert_to_dict(data):
    with open(data, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        lst2 = []
        for each in lines:
            str = each.replace('\n', '')
            lst2.append(str)

    def convert(lst):
        res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
        return res_dct

    return (convert(lst2))


# To make a choice in the dictionary
def choice():
    choice = int(input('Choose your option: \n'
                       '1 - read all records \n'
                       '2 - read 1 student record \n'
                       '3 - update student resord \n'
                       '\n'))
    return (choice)


# To read all of the records from the dict
def read_all(dic):
    for key, value in dic.items():
        print(f'{key}, оценка {value}')

    # To read just 1 specific record from the dict


def read_one(dic):
    student = input('Enter full student name you are looking for: \n')
    if student in dic:
        print(f'{student}, mark {dic[student]}')
    else:
        print('No such student')

    # To change the mark


def change_mark(dict):
    key = input('Name: ')
    new_mark = int(input('New mark: '))

    if key in dict:
        dict[key] = new_mark
    else:
        print('No student found')


lesson = 0
lesson = int(input('Enter the lesson you are looking for: \n'
                   '1 - algebra \n'
                   '2 - literature \n'
                   '3 - chemistry \n'
                   '\n'
                   ))

if lesson == 1:
    # конвертируем файл text в словарь
    data = 'algebra.txt'
    algebra = convert_to_dict(data)

    chosen = choice()

    if chosen == 1:
        read_all(algebra)
    elif chosen == 2:
        read_one(algebra)
    elif chosen == 3:
        change_mark(algebra)
    else:
        print('oopsie, your choice is incorrect')




elif lesson == 2:
    literature = {
        'Ivanov Ivan Kateevich': 2,
        'Petrov Oleg Kosta': 4,
        'Sidorov Leonardo Oleseavich': 3,
        'Ololl Ololosha Igor': 5,
    }
    for key, value in literature.items():
        print(f'{key}, оценка {value}')


elif lesson == 3:
    chemistry = {
        'Ivanov Ivan Kateevich': 5,
        'Petrov Oleg Kosta': 2,
        'Sidorov Leonardo Oleseavich': 3,
        'Ololl Ololosha Igor': 4,
    }
    for key, value in chemistry.items():
        print(f'{key}, оценка {value}')



