line_count = 0
syms_count = 0
with open("people.txt", "r", encoding="utf8") as people_file:
    for i_line in people_file:
        line_count += 1
        len_line = len(i_line.strip())
        if len_line < 3:
            print("Ошибка! В строке", line_count, "имя длиной менее 3-х символов!")
        syms_count += len_line
print("Найденная сумма символов:", syms_count)