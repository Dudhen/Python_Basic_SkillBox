import os

text = input("Введите строку: ")

way = input("Введите последовательность папок через пробел:\n").split()

file_name = input("Введите имя файла: ")
file_name += ".txt"

file_way = os.path.abspath(os.sep)

for i_elem in way:
    file_way = os.path.join(file_way, i_elem)

fw_and_fn = os.path.join(file_way, file_name)

if os.path.exists(file_way):
    if os.path.exists(fw_and_fn):
        question = input("Вы действительно хотите перезаписать файл?\n: ").lower()
        if question == "да":
            file = open(fw_and_fn, "w")
            file.write(text)
            print("Файл успешно перезаписан!")
            file.close()
        else:
            print("Отмена операции.")
    else:
        file = open(fw_and_fn, "w")
        file.write(text)
        print("Файл успешно сохранен!")
        file.close()
else:
    print("Указанного пути не существует на диске!")

# зачетно
