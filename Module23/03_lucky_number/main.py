import random

exceptions = [BaseException, BufferError, MemoryError, OSError, RuntimeError,
              SyntaxError, ValueError, Warning, SyntaxWarning, ResourceWarning]

with open("numbers.txt", "a", encoding="utf8") as numbs_file:
    summ = 0
    while summ < 777:
        numb = int(input("Введите число: "))
        random_numb = random.randint(1, 13)
        if random_numb == 4:
            excep = random.choice(exceptions)
            raise excep("*Текст случайного исключения*")
        numbs_file.write("{}\n".format(numb))
        summ += numb