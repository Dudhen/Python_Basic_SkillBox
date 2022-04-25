countOrder = int(input("Введите кол-во заказов: "))

orders = dict()

for i_order in range(countOrder):
    pizza = dict()
    print(i_order + 1, "заказ: ", end="")
    order = input().split()
    pizza[order[1]] = order[2]
    if order[0] in orders.keys():
        pizzaHave = False
        for pizzaName in orders.values():
            if pizzaName.keys() == pizza.keys():
                pizzaHave = True
                break
        if pizzaHave:
            orders[order[0]][order[1]] = int(orders[order[0]][order[1]]) + int(
                order[2])  # Не знаю что в этом месте не нравится
        else:  # питону, но у меня все работает)
            orders[order[0]][order[1]] = order[2]  # В чем причина?
    else:
        orders[order[0]] = pizza

for people in sorted(orders):
    print(people + ":")
    for i_pizza in sorted(orders[people]):
        print(" " * len(people), i_pizza + ":", orders[people][i_pizza])

# зачтено
