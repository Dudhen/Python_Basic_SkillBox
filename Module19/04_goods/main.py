goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

itemsCount = 0
moneyCount = 0

for i_name in goods:
    item = goods[i_name]
    i = 0
    for i_item in store[item]:
        itemsCount += i_item["quantity"]
        moneyCount += i_item["price"] * i_item["quantity"]
        i += 1
    print(i_name, "-", itemsCount, "шт, стоимость", moneyCount, "руб.")
    itemsCount = 0
    moneyCount = 0

# зачтено
