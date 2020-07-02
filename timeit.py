from time import time


def time_it(func):
    def func_wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        end = time()
        elapsed_time = end - start
        print(f'Function {func.__name__} took {elapsed_time*1000} ms')
    return func_wrapper
