cnt = 0

def decorator(func):
    def decorated(pattern, next_coroutine):
        global cnt
        gen = func(pattern, next_coroutine)
        next(gen)
        try:
            while True:
                line = (yield)
                gen.send(line)
                cnt += 1

        except GeneratorExit:
            next_coroutine.close()
            print(cnt)
    return decorated

@decorator
def match_filter(pattern, next_coroutine):
    print('Looking for ' + pattern)
    try:
        while True:
            s = (yield)
            if pattern in s:
                next_coroutine.send(s)
    except GeneratorExit:
        next_coroutine.close()


def print_consumer():
    print('Preparing to print')
    try:
        while True:
            line = (yield)
            print(line)
    except GeneratorExit:
        print("=== Done ===")

#build producer
def read(text, next_coroutine):
    for line in text.split():
        next_coroutine.send(line)
    next_coroutine.close()

text = 'Commending spending is offending to people pending lending'

printer = print_consumer()
printer.__next__()
matcher = match_filter('pend', printer)
matcher.__next__()
read(text, matcher)