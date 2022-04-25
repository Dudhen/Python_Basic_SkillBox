class Squad:
    def __init__(self, numb: int, start=1):
        self.numb = numb
        self.start = start

    def __iter__(self):
        self.start = 0
        return self

    def __next__(self):
        self.start += 1
        if self.start > self.numb:
            raise StopIteration
        return self.start ** 2


def my_squad(number: int):
    start_int = 0
    for _ in range(number):
        start_int += 1
        yield start_int ** 2


numb_N = int(input("Введите число: "))
my_iterator = Squad(numb_N)
for i_value in my_iterator:
    print(i_value, end=" ")

print()

my_generator = my_squad(numb_N)
for i_value in my_generator:
    print(i_value, end=" ")

print()

squads_nums = (num ** 2 for num in range(1, numb_N + 1))
for i_value in squads_nums:
    print(i_value, end=" ")

# зачтено
