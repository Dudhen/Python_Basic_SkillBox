def move(disks, start, support, final):
    if disks == 1:
        print('Переложить диск 1 со стержня {} на стержень {}'.format(start, final))
        return
    move(disks - 1, start, final, support)
    print('Переложить диск {} со стержня {} на стержень {}'.format(disks, start, final))
    move(disks - 1, support, start, final)


N = int(input("Введите количество дисков: "))
X = int(input("Введите номер стержня, с которой начнется игра\n(всего 3 стрержня): "))
Y = int(input("Введите номер стержня, на которой игра закончится\n(всего 3 стрержня): "))
Z = 6 - (X + Y)

move(N, X, Z, Y)

# зачтено
