def isSimpleIndx(iterrableObject):
    return [num[0] for num in enumerate(iterrableObject) if is_prime(num[0]) == "is simple numb"]


def is_prime(numb):
    i = 0
    for dev in range(1, numb):
        if numb % dev == 0:
            i += 1
    if i == 1:
        return "is simple numb"


object = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# object = ("А", "Р", "С", "Е", "Н", "И", "Й")
# object = {"А", "Р", "С", "Е", "Н", "И", "Й"}
# object = "АРСЕНИЙ"

print(isSimpleIndx(object))

# зачтено
