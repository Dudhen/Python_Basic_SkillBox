import zipfile

z = zipfile.ZipFile('voyna-i-mir.zip', 'r')

z.extract("voyna-i-mir.txt")

z.close()

file_text = open("voyna-i-mir.txt", "r", encoding="UTF-8")

reader = file_text.read()

lets = {}

for i_let in reader:
    if i_let.isalpha() and not i_let in lets:
        lets[i_let] = reader.count(i_let)

result = {}

file_text.close()

for i_value in sorted(lets.values(), reverse=True):
    for i_key in lets.keys():
        if lets[i_key] == i_value:
            result[i_key] = [i_value]

result_file = open("result.txt", "w", encoding="UTF-8")
result_file.write("Статистика по буквам в романе \"Война и мир\":\n\n")
for i_let, i_let_count in result.items():
    result_file.write(i_let + ": ")
    result_file.write(str(i_let_count[0]) + "\n")
result_file.close()

result_file = open("result.txt", "r", encoding="UTF-8")

for i_line in result_file:
    print(i_line, end="")

result_file.close()

# зачтено
