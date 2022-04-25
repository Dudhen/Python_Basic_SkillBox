from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

result_floats = list(map(lambda x: round(x ** 3, 3), floats))
result_names = list(filter(lambda name: len(name) >= 5, names))
result_numbers = reduce(lambda a, b: a * b, numbers)
print("Числа из списка floats в кубе с округлением в три знака после запятой:", result_floats)
print("Имена из списка names, в которых есть хотя бы 5 букв:", result_names)
print("Произведение всех чисел из списка numbers:", result_numbers)

# зачтено
