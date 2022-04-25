class Water:

    def __init__(self, name="Вода"):
        self.name = name

    def __add__(self, other):
        if other.name == "Огонь":
            return Steam()
        elif other.name == "Воздух":
            return Storm()
        elif other.name == "Земля":
            return Dirt()


class Fire:

    def __init__(self, name="Огонь"):
        self.name = name

    def __add__(self, other):
        if other.name == "Вода":
            return Steam()
        elif other.name == "Воздух":
            return Light()
        elif other.name == "Земля":
            return Lava()
        elif other.name == "Грязь":
            return Stone()


class Air:

    def __init__(self, name="Воздух"):
        self.name = name

    def __add__(self, other):
        if other.name == "Земля":
            return Dust()
        elif other.name == "Вода":
            return Storm()
        elif other.name == "Огонь":
            return Light()


class Earth:

    def __init__(self, name="Земля"):
        self.name = name

    def __add__(self, other):
        if other.name == "Воздух":
            return Dust()
        elif other.name == "Вода":
            return Dirt()
        elif other.name == "Огонь":
            return Lava()


class Steam:
    answer = "Сложили Воду и Огонь и вывели Пар"


class Dust:
    answer = "Сложили Воздух и Землю и вывели Пыль"


class Storm:
    answer = "Сложили Воздух и Воду и вывели Шторм"


class Dirt:

    def __init__(self, name="Грязь", is_on=False):
        self.name = name
        self.is_on = is_on

    def __add__(self, other):
        if self.is_on:
            if other.name == "Огонь":
                return Stone()

    answer = "Сложили Воду и Землю и вывели Грязь"


class Light:
    answer = "Сложили Воздух и Огонь и вывели Молнию"


class Lava:
    answer = "Сложили Огонь и Землю и вывели Лаву"


class Stone:
    answer = "Сложили Огонь и Грязь и вывели Камень"


water = Water()
fire = Fire()
earth = Earth()
air = Air()
result = water + fire
print(result.answer)
result = water + air
print(result.answer)
result = water + earth
print(result.answer)
dirt = Dirt(is_on=True)
result = dirt + fire
print(result.answer)
result = air + fire
print(result.answer)
result = air + earth
print(result.answer)
result = earth + fire
print(result.answer)

# зачтено
