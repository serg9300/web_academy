def alphabet_generator():
    current = 'a'
    while current<='z':
        yield current
        current = chr(ord(current)+1)

d=alphabet_generator()
for i in d:
    print(i)
