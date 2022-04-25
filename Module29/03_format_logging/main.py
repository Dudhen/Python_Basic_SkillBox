import functools
from datetime import datetime
import time


def log_methods(str):
    def decorator(cls, str_2):
        @functools.wraps(cls)
        def wrapped(*args, **kwargs):
            i_datetime = datetime.utcnow()
            valid_str = ""
            for i_sym in str:
                if i_sym.isalpha():
                    valid_str += "%" + i_sym
                else:
                    valid_str += i_sym
            datetime_str = i_datetime.strftime(valid_str)
            print("Запускается \'{}.{}\'. Дата и время запуска: {}".format(str_2, cls.__name__, datetime_str))
            start = time.time()
            result = cls(*args, **kwargs)
            end = time.time()
            print("Завершение \'{}.{}\', время работы = {}s".format(str_2, cls.__name__, round(end - start, 3)))
            return result

        return wrapped

    return decorator


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method in dir(cls):
            if not i_method.startswith("__"):
                method = getattr(cls, i_method)
                decorated_method = decorator(method, str(cls.__name__))
                setattr(cls, i_method, decorated_method)
        return cls

    return decorate


@for_all_methods(log_methods("b d Y - H:M:S"))
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test_sum_1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@for_all_methods(log_methods("b d Y - H:M:S"))
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test_sum_1 у наследника")

    def test_sum_2(self):
        print("Тут метод test_sum_2 у наследника")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

# зачтено
