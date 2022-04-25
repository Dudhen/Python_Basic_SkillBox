countPair = int(input("Введите количество пар слов: "))

lib = dict()

for i_pair in range(countPair):
    print(i_pair + 1, "пара: ", end="")
    pair = input().lower().split(" - ")
    lib[pair[0]] = pair[1]
    lib[pair[1]] = pair[0]

print()
good = False
while not good:
    word = input("Введите слово: ").lower()
    if word in lib:
        print("Синоним:", lib[word])
        good = True
    else:
        print("Такого слова в словаре нет.")

# зачтено
