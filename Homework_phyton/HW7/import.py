# функция импорта в наш файл

def import_():
    lst = []
    with open('for_import.txt', 'r', encoding='UTF-8') as f:
        for line in f:
            lst.append(line)
    print(lst)

    with open('file_for.txt', 'a', encoding='UTF-8') as f:
        for i in lst:
            f.write(f'{i}')

import_()
