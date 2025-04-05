def my_decorator(func):
    def wrapper():
        print("Что то происходит перед вызовом функции")
        func()
        print("Что то происходит после функции")

    return wrapper()


@my_decorator
def Hello():
    print("Привет!")


Hello
