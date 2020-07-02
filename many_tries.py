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
