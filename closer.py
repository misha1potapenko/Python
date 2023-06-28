

def add_one(a):
    names = []

    def add_two(b):
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two

hello = add_one('Helolo')
print(hello("Alex"))
print(hello('Masha'))


def add_one_nonlocal(a):

    text = ''

    def add_two_nonlocal(b):
        nonlocal text
        text += ', ' + b
        return a + text
    return add_two_nonlocal

hello = add_one_nonlocal('Helolo')
print(hello("Alex"))
print(hello('Masha'))