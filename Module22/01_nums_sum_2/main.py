numbers_file = open("numbers.txt", "r")
count = 0
for i_line in numbers_file:
    for i_elem in i_line:
        if i_elem.isdigit():
            count += int(i_elem)
numbers_file.close()

count_numbs = open("answer.txt", "w")
count_numbs.write(str(count))
count_numbs.close()

# зачтено
