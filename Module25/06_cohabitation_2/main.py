import random


class Person:
    food_count = 0

    def __init__(self, name, house, satiety=50, happiness=100, is_died=False, depression=False):
        self.name = name
        self.house = house
        self.satiety = satiety
        self.is_died = is_died
        self.happiness = happiness
        self.depression = depression

    def pet_the_cat(self):
        self.happiness += 5
        self.satiety -= 10

    def eating(self):
        if self.house.fridge < 30:
            self.satiety += self.house.fridge
            self.house.fridge = 0
            self.food_count += self.house.fridge
        else:
            self.satiety += 30
            self.house.fridge -= 30
            self.food_count += 30


class Husband(Person):
    money_count = 0

    def playing(self):
        self.satiety -= 10
        self.happiness += 20

    def working(self):
        self.satiety -= 10
        self.house.money += 150
        self.money_count += 150

    def life(self):
        if self.satiety <= 0:
            self.is_died = True
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.happiness < 10:
            self.depression = True
            self.is_died = True
        cube = random.randint(1, 6)
        if self.satiety < 15:
            self.eating()
            print("Муж {} поел. Еды в холодильнике осталось {} единиц, а сытость теперь {} единиц".format(
                self.name,
                self.house.fridge,
                self.satiety)
            )
        elif self.house.money < 100:
            self.working()
            print("Муж {} сегодня работал. Денег в доме теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.house.money,
                self.satiety)
            )
        elif self.happiness < 50:
            self.playing()
            print("Муж {} сегодня играл. Уровень счастья у него теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.happiness,
                self.satiety)
            )
        elif cube == 1:
            self.working()
            print("Муж {} сегодня работал. Денег в доме теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.house.money,
                self.satiety)
            )
        elif cube == 2:
            self.eating()
            print("Муж {} поел. Еды в холодильнике осталось {} единиц, а сытость теперь {} единиц".format(
                self.name,
                self.house.fridge,
                self.satiety)
            )
        else:
            self.pet_the_cat()
            print(
                "Муж {} сегодня гладил кота и играл с ним."
                " Уровень счастья теперь {} единиц, а сытости {} единиц".format(
                    self.name,
                    self.happiness,
                    self.satiety)
            )


class Wife(Person):
    def __init__(self, name, house, fur_coats=0):
        super().__init__(name, house)
        self.fur_coats = fur_coats

    def go_market(self):
        if self.house.food_cat < 50:
            self.house.food_cat += 15
            self.house.money -= 15
        self.house.fridge += 50
        self.house.money -= 50
        self.satiety -= 10

    def buy_fur_coat(self):
        self.fur_coats += 1
        self.house.money -= 350
        self.satiety -= 10
        self.happiness += 60

    def clean_house(self):
        if self.house.dirt <= 100:
            self.house.dirt = 0
        else:
            self.house.dirt -= 100
        self.satiety -= 10

    def life(self):
        if self.satiety <= 0:
            self.is_died = True
        if self.house.dirt > 90:
            self.happiness -= 10
        if self.happiness < 10:
            self.depression = True
            self.is_died = True
        if self.satiety < 15:
            self.eating()
            print("Жена {} поела. Еды в холодильнике осталось {} единиц, а сытость теперь {} единиц".format(
                self.name,
                self.house.fridge,
                self.satiety)
            )
        elif self.house.fridge < 50:
            self.go_market()
            print("Жена {} сегодня ходила в магазин. Еды для людей в доме теперь {} единиц, для кота {} единиц,"
                  " денег в доме {} единиц, а ее сытость теперь {} единиц.".format(
                self.name,
                self.house.fridge,
                self.house.food_cat,
                self.house.money,
                self.satiety))
        elif self.happiness < 50 or self.house.money > 400:
            self.buy_fur_coat()
            print("Жена {} сегодня купила себе {}-ю шубу."
                  " Уровень счастья у нее теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.fur_coats,
                self.happiness,
                self.satiety))
        elif self.house.dirt > 100:
            self.clean_house()
            print("Жена {} сегодня убирала дом. Грязи в доме теперь {} единиц, а сытость теперь {} единиц.".format(
                self.name,
                self.house.dirt,
                self.satiety)
            )
        else:
            self.pet_the_cat()
            print(
                "Жена {} сегодня гладила кота и играла с ним."
                " Уровень счастья теперь {} единиц, а сытости {} единиц".format(
                    self.name,
                    self.happiness,
                    self.satiety)
            )


class Cat:
    cat_food_count = 0

    def __init__(self, name, house, satiety=30, is_died=False):
        self.name = name
        self.satiety = satiety
        self.house = house
        self.is_died = is_died
        if self.satiety <= 0:
            self.is_died = True

    def eating(self):
        self.satiety += 20
        self.house.food_cat -= 10
        self.cat_food_count += 10

    def sleep(self):
        self.satiety -= 10

    def rip_wallpaper(self):
        self.satiety -= 10
        self.house.dirt += 5

    def life(self):
        self.house.dirt += 5
        cube = random.randint(1, 2)
        if self.satiety < 15:
            self.eating()
            print("Кот {} поел. Еды у кота осталось {} единиц, а сытость теперь {} единиц".format(
                self.name,
                self.house.food_cat,
                self.satiety)
            )
        elif self.satiety > 40:
            self.sleep()
            print("Кот {} сегодня спал. Его сытость теперь {} единиц.".format(
                self.name,
                self.satiety))
        elif cube == 2:
            self.rip_wallpaper()
            print("Кот {} сегодня рвала обои. Грязи в доме теперь {} единиц, а его сытость теперь {} единиц.".format(
                self.name,
                self.house.dirt,
                self.satiety)
            )
        elif cube == 1:
            self.sleep()
            print("Кот {} сегодня спал. Его сытость теперь {} единиц.".format(
                self.name,
                self.satiety))


class House:
    def __init__(self, fridge=50, money=100, food_cat=30, dirt=0):
        self.fridge = fridge
        self.money = money
        self.dirt = dirt
        self.food_cat = food_cat


house = House()
husband = Husband("Артем", house)
wife = Wife("Диана", house)
cat = Cat("Барсик", house)

good = True

for i_day in range(1, 366):
    print("День {}:".format(i_day))
    husband.life()
    wife.life()
    cat.life()
    if husband.is_died or wife.is_died or cat.is_died:
        if husband.is_died:
            if husband.depression:
                print("Муж {} умер от депрессии. Эксперимент Закончен.".format(husband.name))
            else:
                print("Муж {} умер от голода. Эксперимент Закончен.".format(husband.name))
        if wife.is_died:
            if wife.depression:
                print("Жена {} умерла от депрессии. Эксперимент Закончен.".format(wife.name))
            else:
                print("Жена {} умерла от голода. Эксперимент Закончен.".format(wife.name))
        if cat.is_died:
            print("Кот {} умер от голода. Эксперимент Закончен.".format(cat.name))
        good = False
        break

if good:
    print("\nЭксперимент закончен успешно!\nДенег скоплено {} единиц, в холодильнике осталось {} единиц еды,"
          " а шуб куплено {} единиц.\n"
          "За все время было:\n"
          "Съедено человеческой еды: {} единиц\n"
          "Съедено кошачьей еды: {} единиц\n"
          "Заработано всего денег: {} единиц\n"
          "Уровень счастья мужа: {} единиц\n"
          "Уровень счастья жены: {} единиц.".format(
        house.money,
        house.fridge,
        wife.fur_coats,
        wife.food_count + husband.food_count,
        cat.cat_food_count,
        husband.money_count,
        husband.happiness,
        wife.happiness))

# зачтено
