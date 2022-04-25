from collections.abc import Callable


def decorator_with_args_for_any_decorator(decorated_func):
    def wrapped(*args, **kwargs):
        def wrapper(func):
            return decorated_func(func, *args, **kwargs)

        return wrapper

    return wrapped


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    def wrapped(*args_2, **kwargs_2):
        print("Переданные арги и кварги:", args_2, kwargs_2)
        result = func(*args_2, **kwargs_2)
        return result

    return wrapped


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# зачтено
