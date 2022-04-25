import random
import time

GAME_STATE = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def draw_state(game_state):
    print("\n\n{}\n".format("-" * 20))
    first_step = True
    for i in game_state:
        if i != " ":
            first_step = False
            break

    numbs = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    p = 0
    for i_col in range(3):
        i = 0
        q = 0
        q += p
        for i_row in range(5):
            if i_row % 2 == 0:
                if first_step:
                    print(" {} ".format(numbs[i_col][i_row - i]), end="")
                else:
                    print(" {} ".format(game_state[q]), end="")
                    q += 1
                i += 1
            else:
                print("|", end="")
        p += 3
        if i_col < 2:
            print("\n---+---+---")


def get_bot_move(game_state):
    while True:
        a = random.randint(0, 8)
        if game_state[a] == " ":
            return a


def check(game_state, a, b, c):
    if game_state[a] == "x" and game_state[b] == "x" and game_state[c] == "x":
        return "x"
    elif game_state[a] == "o" and game_state[b] == "o" and game_state[c] == "o":
        return "o"


def get_winner(game_state):
    i = []
    if i.count("o") == 0 and i.count("x") == 0:
        i.append(check(game_state, 0, 1, 2))
        i.append(check(game_state, 3, 4, 5))
        i.append(check(game_state, 6, 7, 8))
        i.append(check(game_state, 0, 3, 6))
        i.append(check(game_state, 1, 4, 7))
        i.append(check(game_state, 2, 5, 8))
        i.append(check(game_state, 0, 4, 8))
        i.append(check(game_state, 2, 4, 6))
    if i.count("x") > 0:
        return "\nВы собрали линию крестиками и выиграли! Игра окончена!"
    if i.count("o") > 0:
        return "\nВы проиграли. Нолики собрали линию. Игра окончена!"
    if game_state.count(" ") == 0 and i.count("x") == 0 and i.count("o") == 0:
        return "\nУ Вас с ботом ничья!"
    if game_state.count(" ") > 0 and i.count("o") == 0 and i.count("x") == 0:
        return None


def process(game_state):
    draw_state(game_state)
    your_step = int(input("\n\nСейчас ваш ход! Выберете номер клеточки: "))
    if game_state[your_step - 1] == " ":
        game_state[your_step - 1] = "x"
    else:
        while True:
            your_step = int(input(
                "\nВы ввели уже занятой номер клеточки!\nПожалуйста, выберете свободный номер клеточки: "))
            if game_state[your_step - 1] == " ":
                game_state[your_step - 1] = "x"
                break
    if get_winner(game_state):
        draw_state(game_state)
        print("\n{}".format(get_winner(game_state)))
    else:
        print("\nПодождите немного, сейчас ход БОТа...")
        time.sleep(2)
        game_state[get_bot_move(game_state)] = "o"
        if get_winner(game_state):
            draw_state(game_state)
            print("\n{}".format(get_winner(game_state)))
        else:
            process(game_state)


print("\nДобро пожаловать в игру \"Крестики-Нолики\"!\nКак играть:\nВы играете за крестики.")
print("\nВведите номер клеточки куда хотите сделать ход (цифры уберутся после первого хода).")
print("После этого дайте время БОТу на ход (2-3 секунды), и если игра не будет завершена, то ходите снова!)", end="")
process(GAME_STATE)

# зачтено
