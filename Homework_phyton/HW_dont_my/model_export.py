def file_exp(data):    
    with open(data, "r", encoding='utf-8') as f:
        with open('phone_book_exp.txt', "w", encoding='utf-8') as g:
            for line in f:
                g.write(line)