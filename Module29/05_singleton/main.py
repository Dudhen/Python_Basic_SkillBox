import functools


def singleton(cls):
    cls.count = 0
    cls.instance = None

    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        cls.count += 1
        if cls.count == 1:
            cls.instance = cls(*args, **kwargs)
        return cls.instance

    return wrapped


@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

# зачтено
