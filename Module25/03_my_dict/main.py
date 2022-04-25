class MyDict:

    def __init__(self, string):
        self.string = dict(string)

    def get(self, string):
        if string in self.string.keys():
            return self.string[string]
        else:
            return 0


_dict = {"a": 6}
print(_dict.get("a"))
print(_dict.get("b"))
my_dict = MyDict(_dict)
print(my_dict.get("a"))
print(my_dict.get("б"))

# зачтено
