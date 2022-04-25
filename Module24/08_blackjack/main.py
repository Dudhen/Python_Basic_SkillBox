import random


class Player:

    def __init__(self, name, cards, summ=0):
        self.name = name
        self.summ = summ
        self.cards = cards


class Card:

    def __init__(self, name, price):
        self.name = name
        self.price = price


card_2 = Card("2", 2)
card_3 = Card("3", 3)
card_4 = Card("4", 4)
card_5 = Card("5", 5)
card_6 = Card("6", 6)
card_7 = Card("7", 7)
card_8 = Card("8", 8)
card_9 = Card("9", 9)
card_10 = Card("10", 10)
card_jack = Card("Валет", 10)
card_lady = Card("Дама", 10)
card_king = Card("Король", 10)
card_ace = Card("Туз", 11)

cards_list = [card_2, card_3, card_4, card_5, card_6, card_7, card_8, card_9, card_10,
              card_jack, card_lady, card_king, card_ace]

name = input("Введите имя игрока: ")
print("\nДобро пожаловать в игру Блэкджек, {}!".format(name))

player_1 = Player(name, [])
croupier = []

for i in range(1, 5):
    i_card = random.choice(cards_list)
    if i == 1 or i == 3:
        player_1.cards.append(i_card)
        player_1.summ += i_card.price
        cards_list.remove(i_card)
    else:
        croupier.append(i_card)
        cards_list.remove(i_card)

i = 0
cards_croupier = list()

for i_card in croupier:
    i += i_card.price
    cards_croupier.append(i_card.name)

need_next_message = True

ace_in_playerCards = False

while True:
    your_cards = list()
    your_cards.clear()
    for i_card_name in player_1.cards:
        your_cards.append(i_card_name.name)
    if player_1.summ == 21:
        print("\n{}, у Вас ровно 21 очко! Вы выиграли!".format(player_1.name))
        print("Ваши карты {}".format(your_cards))
        need_next_message = False
        break
    print("\nУ вас на руках {}. Ваша сумма очков: {}".format(your_cards, player_1.summ))
    question = input("Введите действие (взять карту или остановиться): ").lower()
    if question == "взять карту":
        i_card = random.choice(cards_list)
        player_1.cards.append(i_card)
        cards_list.remove(i_card)
        your_cards.append(i_card.name)
        player_1.summ += i_card.price
        if player_1.summ > 21:
            if "Туз" in your_cards:
                if not ace_in_playerCards:
                    player_1.summ -= 10
                    ace_in_playerCards = True
                else:
                    print("\n{}, у Вас больше чем 21 очко! Вы проиграли".format(player_1.name))
                    print("Ваши карты {}".format(your_cards))
                    print("Карты крупье: {}".format(cards_croupier))
                    need_next_message = False
                    break
            else:
                print("\n{}, у Вас больше чем 21 очко! Вы проиграли".format(player_1.name))
                print("Ваши карты {}".format(your_cards))
                print("Карты крупье: {}".format(cards_croupier))
                need_next_message = False
                break
    elif question == "остановиться":
        break
    else:
        print("Ошибка ввода! Пожалуйста, введите \"взять карту\" или \"остановиться\"")

if need_next_message:
    if player_1.summ > i:
        print("\n{}, Вы выиграли! У Вас {} очков, а у крупье {} очков.".format(player_1.name, player_1.summ, i))
        print("Карты крупье: {}".format(cards_croupier))
    elif player_1.summ < i:
        print("\n{}, Вы проиграли. У Вас {} очков, а у крупье {} очков.".format(player_1.name, player_1.summ, i))
        print("Карты крупье: {}".format(cards_croupier))
    else:
        print("\n{}, у Вас ничья. У Вас {} очков, а у крупье {} очков.".format(player_1.name, player_1.summ, i))
        print("Карты крупье: {}".format(cards_croupier))

# зачтено
