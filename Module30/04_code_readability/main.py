# TODO здесь писать код
result_1 = " ".join([str(numb) for numb in range(1001) if len([n for n in range(1, numb + 1) if numb % n == 0]) == 2])
print(result_1)


def check_is_simple(n: int) -> int:
    i = 0
    for i_numb in range(1, n + 1):
        if n % i_numb == 0:
            i += 1
    return i


def process(numb: int) -> str:
    result = ""
    for i_numb in range(1, numb + 1):
        if check_is_simple(i_numb) == 2:
            result += str(i_numb) + " "
    return result


print(process(1000))

# зачтено
