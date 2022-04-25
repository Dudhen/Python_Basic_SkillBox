text_file = open("text.txt", "r")

analyst_file = open("analysis.txt", "w")

lets_list = list()
text = str()

print("Содержимое файла text.txt:")

for i_line in text_file:
    print(i_line)
    for i_let in i_line.lower():
        if not i_let in lets_list and i_let.isalpha():
            lets_list.append(i_let)
        if i_let.isalpha():
            text += i_let
print()
text_file.close()

analysts_info = dict()

for i_let in lets_list:
    result = text.count(i_let) / len(text)
    analysts_info[i_let] = round(result, 3)

result = dict()

for i_value in sorted(analysts_info.values(), reverse=True):
    for i_key in sorted(analysts_info.keys()):
        if analysts_info[i_key] == i_value:
            result[i_key] = [i_value]

for i_key, i_value in result.items():
    analyst_file.write(i_key + " ")
    analyst_file.write(str(i_value[0]) + "\n")
analyst_file.close()

analyst_file = open("analysis.txt", "r")
print("Содержимое файла analysis.txt:")
print(analyst_file.read())
analyst_file.close()

# зачтено
