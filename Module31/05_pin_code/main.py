import itertools

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

result = list()

for numb in itertools.product(numbers, numbers):
    result.append(numb)

i = 0
for numb in itertools.product(result, result):
    i += 1
    print(numb[0][0],
          numb[0][1],
          numb[1][0],
          numb[1][1])

# зачтено
