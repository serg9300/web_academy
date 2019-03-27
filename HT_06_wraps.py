from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        #print(func.__doc__)
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """this is functools.wraps"""
   return x + x * x

print(f.__name__)  # prints 'f'
print(f.__doc__)  # prints 'does some math'
f(5)