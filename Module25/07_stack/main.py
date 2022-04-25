class Stack:
    def __init__(self, i_list=[]):
        self.i_list = i_list

    def add_elem(self, elem):
        self.i_list.append(elem)
        print("Список теперь выглядит так: {}".format(self.i_list))

    def delete_last(self):
        self.i_list.remove(self.i_list[-1])
        print("Список теперь выглядит так: {}".format(self.i_list))


first_list = Stack()
first_list.add_elem("кранштейн")
first_list.add_elem("весло")
first_list.add_elem("вертлюг")
first_list.add_elem("уклютчина")
first_list.delete_last()
first_list.delete_last()


class TaskManager:
    def __init__(self, i_dict={}):
        self.i_dict = i_dict

    def new_task(self, task, priority):
        if priority in self.i_dict.keys():
            self.i_dict[priority].append(task)
        else:
            self.i_dict[priority] = [task]

    def print(self):
        print("Результат:")
        for i_key in sorted(self.i_dict):
            if len(self.i_dict[i_key]) == 1:
                print("{}  {}".format(i_key, self.i_dict[i_key][0]))
            else:
                print(i_key, end=" ")
                for i_value in self.i_dict[i_key]:
                    print(i_value, end="; ")
                print()


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.print()

# зачтено
