import functools


def check_permission(user):
    def check_decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if user in user_permissions:
                result = func(*args, **kwargs)
                return result
            else:
                print("PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию {}".format(
                    func.__name__
                ))

        return wrapped

    return check_decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# зачтено
