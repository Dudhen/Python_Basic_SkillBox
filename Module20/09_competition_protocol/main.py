printCount = int(input("Сколько записей вносится в протокол?: "))

players = list()

print("Записи (результат и имя):")
for i_player in range(printCount):
    print(i_player + 1, "запись: ", end="")
    player = input().split()
    players.append(player)

print("\nИтоги соревнований:")
for i in range(1, 4):
    score = 0
    winner = str()
    for i_winner in players:
        if int(i_winner[0]) > score:
            score = int(i_winner[0])
            winner = i_winner[1]
    print(i, "место:", winner, "(" + str(score) + ")")
    for i_out in players:
        if i_out[1] == winner:
            players.remove(i_out)

# зачтено
