import random

random_list = list()

for _ in range(10):
    random_list.append(random.randint(1, 100))

newList = list()

pair = list()

for i_numb in random_list:
    pair.append(i_numb)
    if len(pair) == 2:
        newList.append(tuple(pair))
        pair.clear()

print("Оригинальный список:", random_list)
print("Новый список:", newList)
print()

newList_2 = list()

for i_indx in range(0, 10, 2):
    pair = (random_list[i_indx], random_list[i_indx + 1])
    newList_2.append(pair)

print("Оригинальный список:", random_list)
print("Новый список вторым способом:", newList_2)

# зачтено
