"""
Написать декоратор, сохраняющий последний результат функции в .txt файл с названием функции в имени
"""
def logger(func):
    def wrapped(*args, **kwargs):
        # print(f'[LOG] Вызвана функция {func.__name__} c аргументами: {args}, {kwargs}')
        f_name = func.__name__ + '.txt'
        f = open(f_name, "w")
        result = func(*args)
        f.write(f'Last result: {result}')
        f.close()
        return result
    return wrapped

@logger
def my_func(a):
    c = list(map(lambda x: x ** 3, a))
    return c

a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = my_func(a)
