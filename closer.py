

def add_one(a):
    names = []

    def add_two(b):
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two

hello = add_one('Helolo')
print(hello("Alex"))
print(hello('Masha'))