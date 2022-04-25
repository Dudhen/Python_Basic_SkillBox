def fibonacci(list, n, i=1):
    if i == n:
        print(list[-1])
    else:
        list.append(list[-1] + list[-2])
        fibonacci(list, n, i + 1)


numb = int(input("Введите позицию числа в ряде Фибоначчи: "))

fib_start = [0, 1]

fibonacci(fib_start, numb)

# зачтено
