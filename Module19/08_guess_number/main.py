import random

numbMAX = int(input("Введите максимальное число: "))

numbArtem = random.randint(1, numbMAX)

preResult = set([str(numb) for numb in range(1, numbMAX + 1)])

print("\n(Введите команду \"Помогите!\", чтобы попросить помощи у БОТа)\n(Цифры вводятся через пробел)")

numbsBoris = input("\nНужное число есть среди вот этих чисел?: ").split()
if not numbsBoris[0].isdigit():
    while not numbsBoris[0].isdigit():
        print("Вы не можете запрашивать помощь у БОТа в первый же ход. Введите числа.")
        numbsBoris = input("Нужное число есть среди вот этих чисел?: ").split()

i = 0
while True:
    if numbsBoris[0] == "Помогите!" or len(numbsBoris) == 1 and int(numbsBoris[0]) == numbArtem:
        break
    preResult_1 = set(numbsBoris)
    numbHave = False
    for numb in preResult_1:
        if numbArtem == int(numb):
            numbHave = True
            break
    if numbHave:
        i += 1
        if i == 1:
            preResult = preResult_1
        else:
            variable = preResult_1.difference(preResult)
            preResult = preResult_1
            preResult = preResult.difference(variable)
        print("Ответ Артема: Да")
    else:
        preResult = preResult.difference(preResult_1)
        print("Ответ Артема: Нет")
    numbsBoris = input("\nНужное число есть среди вот этих чисел?: ").split()

if numbsBoris[0] == "Помогите!":
    result = ""
    result_1 = [int(numb) for numb in preResult]
    for i_numb in sorted(result_1):
        result += (str(i_numb) + " ")
    print("Артём мог загадать следующие числа:", result)
elif int(numbsBoris[0]) == numbArtem:
    print("Вы угадали! Загаданное число:", numbArtem)

# зачтено
