class LinkedList:
    def __init__(self, str_="[]"):
        self.str_ = str_

    def append(self, elem):
        self.str_ = self.str_[:-1]
        if len(self.str_) == 1:
            self.str_ += str(elem) + "]"
        else:
            self.str_ += ", " + str(elem) + "]"

    def get(self, index):
        i = 0
        elem = ""
        for i_let in self.str_:
            if index == i:
                elem += i_let
            if i_let == " ":
                i += 1
        return elem[:-1]

    def remove(self, index):
        i = 0
        elem = ""
        for i_let in self.str_:
            if i != index:
                elem += i_let
            if i_let == " ":
                i += 1
        self.str_ = elem


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list.str_)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list.str_)

# зачтено
