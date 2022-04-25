def my_summ(*args, summ=0):
    for i_elem in args:
        if type(i_elem) == int:
            summ += i_elem
        else:
            for elem in i_elem:
                summ += my_summ(elem)
    return summ


print("Ответ:", my_summ([[1, 2, [3]], [1], 3]))

print("Ответ:", my_summ(1, 2, 3, 4, 5))

# зачтено
