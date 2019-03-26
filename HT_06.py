def bread(func):
    def wrapper():
        print()
        func()
        print('<_____>')
    return wrapper
def ingridient(func):
    def wrapper():
        print('Totmatoes')
        func()
        print('Salad')
    return wrapper

@bread
@ingridient
def sandwich(food = 'beef'):
    print(food)
sandwich()
