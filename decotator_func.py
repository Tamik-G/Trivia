def decotator_with_args(func):
    def wrapper(*args):
        print(f"Аргументы функции: {args}")
        result = func(*args)
        print(f"Результат: {result}")
        return result
    return wrapper

@decotator_with_args
def add(a, b):
    return a + b

add(2,3)
add("v", "s")