def imp_column_to_string():
    with open("phone_book_new_2.txt", encoding='utf-8') as f:
        lines = f.readlines()

    with open("book3.txt", "w", encoding='utf-8') as g:
        j = 0
        lst1 = []
        for each in lines:
            if not each.__contains__(','):
                if each != '\n':
                    lst1.append(each.replace("\n", ""))
                    j += 1
                    if j == 4:
                        g.writelines(', '.join(lst1))
                        g.writelines('\n')
                        j = 0
                        lst1 = []


def imp_str_to_column():
    with open("phone_book_new_2.txt", encoding='utf-8') as f:
        lines = f.readlines()

    with open("book3.txt", "w", encoding='utf-8') as g:
        for each in lines:
            if each.__contains__(','):
                str = each.split(',')
                g.writelines('\n'.join(str))
                g.writelines('\n')

