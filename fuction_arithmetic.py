a = input('Enter first number: ')
b = input('Enter second number: ')
calculation = input('Enter argument (+, -, /, *): ')
def arithmetic(a,b,calculation):

    if calculation == '/':
        return int(a)/int(b)
    elif calculation == '*':
        return int(a) * int(b)
    elif calculation == '-':
        return int(a) - int(b)
    elif calculation == '+':
        return int(a) + int(b)
    else:
        return "Unknown operation"
x=arithmetic(a,b,calculation)
print(x)