class Potate:

    def __init__(self, number, rise_status, name="1 картошка", status=str()):
        self.number = number
        self.rise_status = rise_status
        self.name = name
        self.status = status

    def grow_up(self):
        if self.rise_status == 0:
            print("Картошку на ячейке номер {} нужно сначала посадить!".format(self.number))
        else:
            if self.rise_status < 3:
                self.rise_status += 1
                print("Картошка номер {} немного выросла!".format(self.number))
            if self.rise_status == 3:
                print("Картошка номер {} готова к сбору урожая!".format(self.number))

    def check_rise_status(self):
        if self.rise_status == 0:
            self.status = "Нет картошки"
        elif self.rise_status == 1:
            self.status = "Росток"
        elif self.rise_status == 2:
            self.status = "Зеленая"
        elif self.rise_status == 3:
            self.status = "Спелая"
        print("Картошка номер {} находится в состоянии: {}".format(self.number, self.status))


class Potates_garden:

    def __init__(self, number, potates_list=[], good_status=True):
        self.potates_list = potates_list
        self.good_status = good_status
        self.number = number

    def garden_grow_up(self):
        if self.good_status == True:
            for i_potate in self.potates_list:
                if i_potate.rise_status < 3:
                    i_potate.rise_status += 1
                if i_potate.rise_status == 3:
                    print("Картошка номер {} готова к сбору урожая!".format(i_potate.number))
            print("Все картошки на грядке немного выросли!")
        else:
            print("Садовнику нужно сначала поухаживать за грядкой, чтобы грядка начала взращивать картошку!")

    def garden_check_rise_status(self):
        i = 0
        for i_potate in self.potates_list:
            i += i_potate.rise_status
        if len(self.potates_list) == 0 or i == 0:
            print("На грядке в данный момент нет картошки.")
        else:
            for i_potate in self.potates_list:
                i_potate.check_rise_status()


class Gardener:

    def __init__(self, name, gardens=[], harvest=[]):
        self.name = name
        self.gardens = gardens
        self.harvest = harvest

    def care_a_garden(self):
        for i_garden in self.gardens:
            if i_garden.good_status == False:
                i_garden.good_status = True
                print("Садовник {} позаботился о грядке номер {}, грядка ухожена.".format(self.name, i_garden.number))
            else:
                print("Грядка номер {} ухожена, все хорошо. Никаких действий не требуется.".format(i_garden.number))

    def harvesting(self):
        for i_garden in self.gardens:
            for i_potate in i_garden.potates_list:
                if i_potate.rise_status == 3:
                    self.harvest.append(i_potate.name)
                    i_potate.rise_status = 0
        print("Садовник {} собрал все спелые картошки!\nСодержимое корзины: {}".format(self.name, self.harvest))


potate_1 = Potate(1, 1)
potate_2 = Potate(2, 1)
potate_3 = Potate(3, 2)
potate_4 = Potate(4, 2)
potate_5 = Potate(5, 3)
potates_garden_1 = Potates_garden(1, [potate_1, potate_2, potate_3, potate_4, potate_5], False)
gardener_1 = Gardener("Андрей", [potates_garden_1])

print("Добро пожаловать в игру \"Веселая ферма 2.0\"!\n")
potates_garden_1.garden_check_rise_status()
potates_garden_1.garden_grow_up()
gardener_1.care_a_garden()
potates_garden_1.garden_grow_up()
potate_1.check_rise_status()
potate_2.check_rise_status()
potate_3.check_rise_status()
potate_1.grow_up()
potate_2.grow_up()
potates_garden_1.garden_check_rise_status()
gardener_1.harvesting()
potates_garden_1.garden_check_rise_status()

# зачтено
