pairCount = int(input("Введите количество человек: "))

wood = dict()
childrens = list()

names = ""

i = 0
for i_pair in range(1, pairCount):
    print(i_pair, "пара: ", end="")
    pair = input().split()
    if i == 0:
        names += str(pair[1]) + ".0 "
    for i_key in wood.keys():
        if pair[1] == i_key:
            childrens = wood[pair[1]]
        else:
            childrens = []
    wood[pair[1]] = childrens
    children = dict()
    indx = 0
    for List in wood.values():
        i = 0
        for indx_1 in List:
            for person in indx_1:
                if pair[1] == person:
                    indx = List[i][person]
                    break
                i += 1
    children[pair[0]] = indx + 1
    wood[pair[1]].append(children)
    i += 1

for value in wood.values():
    i = 0
    for prePerson in value:
        for person in prePerson:
            names += "".join(str(person))
            numb = str(value[i][person])
        names += "." + numb + " "
        i += 1

names_list = names.split()
names_dict = set(names_list)

print("\n\"Высота\" каждого члена семьи:")
for name in sorted(names_dict):
    name_list = name.split(".")
    print(name_list[0], ":", name_list[1])

# зачтено
