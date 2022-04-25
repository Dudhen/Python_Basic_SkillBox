class Parent:

    def __init__(self, name, age, childs_list=[]):
        self.name = name
        self.age = age
        self.childs_list = childs_list

    def information(self):
        print("Информация обо мне:\nМеня зовут: {}\nМой возраст: {}\nМои дети: {}\n".format(
            self.name,
            self.age,
            [child_name.name for child_name in self.childs_list]
        )
        )

    def calm_child(self, child):
        if child.calm_status_good == False:
            child.calm_status_good = True
            print("Ребенок {} успокоился.".format(child.name))
        else:
            print("Ребенок {} спокоен и не нуждается в успокоении.".format(child.name))

    def feed_child(self, child):
        if child.hunger_status_good == False:
            child.hunger_status_good = True
            print("Ребенок {} покормлен.".format(child.name))
        else:
            print("Ребенок {} не голоден.".format(child.name))


class Child:

    def __init__(self, name, age, calm_status_good=True, hunger_status_good=True):
        self.name = name
        self.age = age
        self.calm_status_good = calm_status_good
        self.hunger_status_good = hunger_status_good


child_1 = Child("Юрий Шестаков", 9, False, False)
child_2 = Child("Алина Шестакова", 5, True, True)
parent_1 = Parent("Максим Шестаков", 32, [child_1, child_2])

parent_1.information()
parent_1.calm_child(child_1)
parent_1.calm_child(child_1)
parent_1.calm_child(child_2)
parent_1.feed_child(child_2)

# зачтено
