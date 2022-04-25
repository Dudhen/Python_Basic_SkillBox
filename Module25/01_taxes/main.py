class Property:
    total_tax = 0

    def __init__(self, worth):
        self.worth = worth
        self.tax = worth


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = self.worth / 200
        Property.total_tax += self.tax


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = self.worth / 1000
        Property.total_tax += self.tax


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.tax = self.worth / 500
        Property.total_tax += self.tax


money = int(input("Введите количество денег в рублях: "))
car = Car(int(input("Введите стоимость машины в рублях: ")))
apart = Apartment(int(input("Введите стоимость квартиры в рублях: ")))
country_house = CountryHouse(int(input("Введите стоимость дачи в рублях: ")))

print("Ваши налоги:\n{} рублей - за машину\n{} рублей - за квартиру\n{} рублей - за дачу".format(car.tax,
                                                                                                 apart.tax,
                                                                                                 country_house.tax))

if money >= Property.total_tax:
    print("Вам хватает денег на оплату налогов.")
else:
    print("На оплату налогов Вам не хватает {} рублей".format(Property.total_tax - money))

# зачтено
