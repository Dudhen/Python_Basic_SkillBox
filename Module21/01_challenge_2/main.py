def nums_list(start, num):
    if start == num:
        return num
    print(start)
    return nums_list(start + 1, num)


numb = int(input("Введите число: "))

print(nums_list(1, numb))

# зачтено
