class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 0


class Worker(Employee):
    def __init__(self, name, surname, age, work_hours):
        super().__init__(name, surname, age)
        self.work_hours = work_hours
        self.salary = 100 * work_hours


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self.salary = 13000


class Agent(Employee):
    def __init__(self, name, surname, age, volume_sales):
        super().__init__(name, surname, age)
        self.volume_sales = volume_sales
        self.salary = 5000 + ((volume_sales / 100) * 5)


manager_1 = Manager("Игорь", "Немчинский", 42)
manager_2 = Manager("Сергей", "Подшивалов", 36)
manager_3 = Manager("Александр", "Корнилов", 33)
agent_1 = Agent("Анастасия", "Карабельщикова", 37, 500000)
agent_2 = Agent("Екатерина", "Потапова", 28, 275000)
agent_3 = Agent("Павел", "Сафонкин", 41, 178430)
worker_1 = Worker("Дмитрий", "Пигарев", 25, 104)
worker_2 = Worker("Филипп", "Синельник", 31, 176)
worker_3 = Worker("Сергей", "Смирнов", 34, 58)

employees = [manager_1, manager_2, manager_3, agent_1, agent_2, agent_3, worker_1, worker_2, worker_3]

for i_emp in employees:
    print("Заработная плата сотрудника: {}".format(i_emp.salary))

# зачтено
