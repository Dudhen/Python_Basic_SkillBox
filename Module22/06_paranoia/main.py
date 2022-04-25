def encrypt(message, k):
    lets_rus_B = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" * abs(k)
    lets_rus_S = lets_rus_B.lower()
    lets_eng_B = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ" * abs(k)
    lets_eng_S = lets_eng_B.lower()
    result = []
    for i_let in message:
        if i_let in lets_rus_B:
            result.append(lets_rus_B[lets_rus_B.find(i_let) + k])
        elif i_let in lets_rus_S:
            result.append(lets_rus_S[lets_rus_S.find(i_let) + k])
        elif i_let in lets_eng_B:
            result.append(lets_eng_B[lets_eng_B.find(i_let) + k])
        elif i_let in lets_eng_S:
            result.append(lets_eng_S[lets_eng_S.find(i_let) + k])
        else:
            result.append(i_let)
    result_str = "".join(result)
    return result_str


file = open("text.txt", "r", encoding="UTF-8")

encrypt_file = open("cipher_text.txt", "w", encoding="UTF-8")

i = 1
print("Содержимое файла text.txt:")
for i_line in file:
    print(i_line, end="")
    encrypt_file.write(encrypt(i_line, i))
    i += 1
print()
encrypt_file.close()

encrypt_file = open("cipher_text.txt", "r", encoding="UTF-8")
encrypt_text_file = encrypt_file.read()
print("\nСодержимое файла cipher_text.txt:")
print(encrypt_text_file)

encrypt_file.close()
file.close()

# зачтено
