a = input('Enter first number: ')
b = input('Enter second number: ')
calculation = input('Enter argument (+, -, /, *): ')
def arithmetic(a,b,calculation):
    if not isinstance(a, (int,float)) or not isinstance(b, (int, float)):
        return "Error"
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

if __name__ == '__main__':
    arithmetic(a,b,calculation)
    arithmetic(a, b, calculation)
    arithmetic(a, b, calculation)
    arithmetic(a, b, calculation)