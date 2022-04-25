file_first_tour = open("first_tour.txt", "r")

file_second_tour = open("second_tour.txt", "w")

print("Содержимое файла first_tour.txt:")
balls = 0
i = 0
peoples_list = dict()
for i_line in file_first_tour:
    if i == 0:
        balls += int(i_line)
    else:
        if int(i_line[-3:-1]) > balls:
            peoples_list[i_line[:-4]] = i_line[-3:-1]
    i += 1
    print(i_line, end="")
print()

file_first_tour.close()

file_second_tour.write(str(len(peoples_list)) + "\n")

for i_num, i_person in enumerate(sorted(peoples_list.items())):
    person = i_person[0].split()
    person[1] = person[1][0]
    result = str(i_num + 1) + ") " + person[1] + ". " + person[0] + " " + i_person[1]
    file_second_tour.write(result + "\n")
file_second_tour.close()

file_second_tour = open("second_tour.txt", "r")

print("\nСодержимое файла second_tour.txt:")
print(file_second_tour.read())
file_second_tour.close()

# зачтено
