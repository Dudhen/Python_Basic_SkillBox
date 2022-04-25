import collections


def can_be_poly(word: str):
    if list(map(lambda x: word.count(x) % 2, word)).count(1) <= 1:
        return True
    return False


def can_be_poly_2(word: str):
    c = collections.Counter()
    for let in word:
        c[let] += 1

    if len([numb for numb in c.values() if numb % 2 != 0]) <= 1:
        return True
    return False


print(can_be_poly('ababc'))
print(can_be_poly('abb'))

print(can_be_poly_2('ababc'))
print(can_be_poly_2('abb'))

# зачтено
