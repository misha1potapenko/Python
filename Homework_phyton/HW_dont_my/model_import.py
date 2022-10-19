import os

def file_imp(data):
    print('Поместите файл из которого нужно импортировать данные в папку')
    file_name = input('Введите название файла, который нужно импортировать \n') 
    if os.path.isfile(file_name):
        with open(file_name, "r", encoding='utf-8') as f, open(data, "a", encoding='utf-8') as g:
            g.writelines('\n')
            for line in f:
                g.writelines(line)
    else:
        print('Объект не найден')
        