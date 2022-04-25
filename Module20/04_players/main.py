players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

result = list()

for i_name, i_nums in players.items():
    preResult = list()
    preResult.extend([word for word in i_name])
    preResult.extend([word for word in i_nums])
    result.append(tuple(preResult))

print(result)

# зачтено
