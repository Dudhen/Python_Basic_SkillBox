def histogram(string):
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def reverseHist(list):
    result = dict()
    for i in list.values():
        letters = []
        for let in list.keys():
            if list[let] == i:
                letters.append(let)
        result[i] = letters
    return result


string = input("Введите текст: ")
hist = histogram(string)

print("Оригинальный словарь частот:")
for i_sym in sorted(hist.keys()):
    print(i_sym, ":", hist[i_sym])

reverseResult = reverseHist(hist)

print("\nИнвертированный словарь частот:")
for j_sym in reverseResult.keys():
    print(j_sym, ":", reverseResult[j_sym])

# зачтено
