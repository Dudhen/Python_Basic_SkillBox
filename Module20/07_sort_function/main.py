def sorting(tupleNumbs):
    good = True
    for i_numb in list(tupleNumbs):
        if not isinstance(i_numb, int):
            good = False
    if good:
        listSort = sorted(list(tupleNumbs))
        return tuple(listSort)
    else:
        return tupleNumbs


numbers = (6, 12, 3, 54, 43, 34, 37, 89)
print(sorting(numbers))

# зачтено
