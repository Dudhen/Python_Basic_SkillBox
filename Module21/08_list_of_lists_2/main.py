nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


# Делать аргументом по умолчанию изменяемый тип данных - правило плохого тона
def nice_funct(my_list, good_list=[]):
    for i_elem in my_list:
        if type(i_elem) == int:
            good_list.append(i_elem)
        else:
            nice_funct(i_elem)
    return good_list

print(nice_funct(nice_list))

# зачтено