# dekorator mierzący czas funkcji
# dekorator który spróbuje wykonać funkcje parę razy
from time import time


def multiply_tries(func):
    def func_wrapper(*args, **kwargs):
        mistakes = 0
        for i in range(5):
            try:
                func(*args, **kwargs)
            except:
                mistakes += 1
        return print(f'There were {mistakes}/5 errors while executing')
    return func_wrapper


def time_it(func):
    def func_wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        elapsed_time = end - start
        print(f'Function {func.__name__} took {elapsed_time*1000} ms')
    return func_wrapper


@time_it
def add_2(n):
    return print(n + 2)


add_2(2)
