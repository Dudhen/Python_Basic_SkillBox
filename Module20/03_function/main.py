def newTuple_by_sym(isTuple, sym):
    syms = list()
    symFound = False
    for i_sym in list(isTuple):
        if symFound:
            syms.append(i_sym)
            if i_sym == sym:
                symFound = False
                break
        elif i_sym == sym:
            syms.append(i_sym)
            symFound = True
    return tuple(syms)


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10)
randomSym = 222

print(newTuple_by_sym(my_tuple, randomSym))

# зачтено
