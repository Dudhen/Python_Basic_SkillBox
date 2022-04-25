import random


class Unit:

    def __init__(self, name, health, index):
        self.name = name
        self.health = health
        self.index = index

    def punch(self, unit):
        unit.health -= 20
        if unit.health <= 0:
            print("{} (Unit {}) атаковал и убил {}а (Unit {}). Игра окончена!".format(self.name,
                                                                                      self.index,
                                                                                      unit.name,
                                                                                      unit.index)
                  )
        else:
            print("{} (Unit {}) атаковал {}а (Unit {}). У {}а (Unit {}) осталось {} очков здоровья.".format(
                self.name, self.index, unit.name, unit.index, unit.name, unit.index, unit.health)
            )


unit_1 = Unit("Воин", 100, 1)
unit_2 = Unit("Воин", 100, 2)

units = (unit_1, unit_2)
units_action = []

while True:
    units_action.append(unit_1)
    units_action.append(unit_2)
    unit_puncher = random.choice(units)
    units_action.remove(unit_puncher)
    unit_puncher.punch(units_action[0])
    if units_action[0].health <= 0:
        break
    units_action.clear()

# зачтено
