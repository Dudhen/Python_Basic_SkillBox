import math


class Auto:
    def __init__(self, x, y, injection):
        self.x = x
        self.y = y
        self.injection = injection

    def move(self, distance):
        if self.injection > 360:
            self.injection %= 360
        a = (90 - self.injection) / 0.9
        b = (math.sqrt((distance ** 2) / 2)) * 2
        if 90 >= self.injection >= 0:
            self.x += (b / 100) * a
            self.y += b - ((b / 100) * a)
        elif 180 >= self.injection > 90:
            self.x -= (b / 100) * a
            self.y += b - ((b / 100) * a)
        elif 270 >= self.injection > 180:
            self.x -= (b / 100) * a
            self.y -= b - ((b / 100) * a)
        elif 360 >= self.injection > 270:
            self.x += (b / 100) * a
            self.y -= b - ((b / 100) * a)
        print("Теперь ТС находится на приблизительно на координатах {}, {}".format(round(self.x, 5), round(self.y, 5)))

    def change_way(self, new_injection):
        self.injection = new_injection


class Bus(Auto):
    def __init__(self, x, y, injection, passengers, money=0):
        super().__init__(x, y, injection)
        self.passengers = passengers
        self.money = money

    def move(self, distance):
        if self.injection > 360:
            self.injection %= 360
        a = (90 - (self.injection % 90)) / 0.9
        b = (math.sqrt((distance ** 2) / 2)) * 2
        if 90 >= self.injection >= 0:
            self.x += (b / 100) * a
            self.y += b - ((b / 100) * a)
        elif 180 >= self.injection > 90:
            self.x -= (b / 100) * a
            self.y += b - ((b / 100) * a)
        elif 270 >= self.injection > 180:
            self.x -= (b / 100) * a
            self.y -= b - ((b / 100) * a)
        elif 360 >= self.injection > 270:
            self.x += (b / 100) * a
            self.y -= b - ((b / 100) * a)
        way_money = (self.passengers * 5) * distance
        self.money += way_money
        print("Теперь ТС находится на приблизительно на координатах {}, {}".format(round(self.x, 5), round(self.y, 5)))
        print("За этот путь вы заработали {} рублей. Всего в автобусе теперь {} рублей".format(
            way_money,
            self.money
        ))

    def sign_in(self, passengers_count):
        self.passengers += passengers_count
        print("На остановке вошло {} пассажиров. Теперь в автобусе {} пассажиров.".format(passengers_count,
                                                                                          self.passengers))

    def out(self, passengers_count):
        self.passengers -= passengers_count
        print("На остановке вышло {} пассажиров. Теперь в автобусе {} пассажиров.".format(passengers_count,
                                                                                          self.passengers))


bus_1 = Bus(0, 0, 315, 5)
bus_1.move(10)
bus_1.sign_in(8)
bus_1.change_way(30)
bus_1.move(15)

# зачтено
