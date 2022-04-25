string = input("Введите строку: ").lower()

stringList = [let for let in string]

letCount = []

for let in stringList:
    letCount.append(stringList.count(let))

i = 0
for i_count in letCount:
    if i_count % 2 == 1:
        i += 1

if i > 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")

# зачтено
