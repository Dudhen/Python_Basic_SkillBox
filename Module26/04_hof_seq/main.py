def QHofstadter(my_list: list, n: int):
    result = my_list[(n - my_list[-1]) - 1] + my_list[(n - my_list[-2]) - 1]
    my_list.append(result)
    yield my_list


i_list = [1, 1]
numb = 3
range_count = int(input("Пожалуйста, введите сколько первых цифр \nпоследовательности Хофштадтера вы хотите увидеть: "))

for _ in range(range_count - 2):
    if i_list == [1, 2]:
        break
    for i in QHofstadter(i_list, numb):
        i_list = i
        numb += 1

print("Первые {} цифр последовательности Хофштадтера: ".format(range_count), end="")
for i_numb in i_list:
    print(i_numb, end=" ")

# зачтено
