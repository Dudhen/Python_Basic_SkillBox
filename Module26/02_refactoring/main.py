list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56


def generation(list_1: list, list_2: list, numb: int):
    for x in list_1:
        for y in list_2:
            result = x * y
            if result != numb:
                yield "{} {} {}".format(x, y, result)
            else:
                yield "{} {} {}\nFound!!!".format(x, y, result)
                return


my_generation = generation(list_1, list_2, to_find)
for i_value in my_generation:
    print(i_value)

# зачтено
