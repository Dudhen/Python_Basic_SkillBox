import random


class Person:

    def __init__(self, name, house, satiety=50, is_died=False):
        self.name = name
        self.house = house
        self.satiety = satiety
        self.is_died = is_died

    def eating(self):
        self.satiety = 50
        self.house.fridge -= 10

    def working(self):
        self.satiety -= 10
        self.house.money += 20
        if self.satiety <= 0:
            self.is_died = True

    def playing(self):
        self.satiety -= 10
        if self.satiety <= 0:
            self.is_died = True

    def go_market(self):
        self.house.fridge += 20
        self.house.money -= 10

    def life(self):
        cube = random.randint(1, 6)
        if self.satiety < 20:
            self.eating()
            print("Человек {} поел. Еды в холодильнике осталось {} единиц, а сытость теперь {} единиц".format(
                self.name,
                self.house.fridge,
                self.satiety)
            )
        elif self.house.fridge < 10:
            self.go_market()
            print(
                "Человек {} сходил в магазин. Еды в холодильнике теперь {} единиц, а денег осталось {} единиц.".format(
                    self.name,
                    self.house.fridge,
                    self.house.money)
            )
        elif self.house.money < 50:
            self.working()
            print("Человек {} сегодня работал. Денег в доме теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.house.money,
                self.satiety)
            )
        elif cube == 1:
            self.working()
            print("Человек {} сегодня работал. Денег в доме теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.house.money,
                self.satiety)
            )
        elif cube == 2:
            self.eating()
            print("Человек {} поел. Еды в холодильнике осталось {} единиц, а сытость теперь {} единиц".format(
                self.name,
                self.house.fridge,
                self.satiety)
            )
        else:
            self.playing()
            print("Человек {} сегодня играл. Уровень сытости теперь {} единиц".format(
                self.name,
                self.satiety)
            )


class House:

    def __init__(self, fridge=50, money=0):
        self.fridge = fridge
        self.money = money


house = House()
artem = Person("Артем", house)
diana = Person("Диана", house)

good = True

for i_day in range(1, 366):
    print("День {}:".format(i_day))
    artem.life()
    diana.life()
    if artem.is_died or diana.is_died:
        if artem.is_died:
            good = False
            print("Артем умер. Эксперимент Закончен.")
        if diana.is_died:
            good = False
            print("Диана умерла. Эксперимент Закончен.")
        break

if good:
    print("\nЭксперимент закончен успешно! Денег скоплено {} единиц, а в холодильнике {} единиц еды.".format(
        house.money,
        house.fridge)
    )

# зачтено
