import functools


def how_are_you(func):
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        print("Как дела? ", end="")
        question = input()
        print("А у меня не очень. Ладно, держи свою функцию.")
        value = func(*args, **kwargs)
        return value

    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()

# зачтено
