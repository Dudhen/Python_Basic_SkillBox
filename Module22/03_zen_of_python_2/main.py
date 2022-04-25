zen_file = open("zen.txt", "r")

text_lets = []
text_words = []
line_count = 0

for i_line in zen_file:
    line_count += 1
    words = i_line.split()
    for i_word in words:
        text_words.append(i_word)
    for i_sym in i_line:
        if i_sym.isalpha():
            text_lets.append(i_sym)

zen_file.close()

let_min = text_lets[0].lower()

for i_let in text_lets:
    if text_lets.count(i_let.lower()) < text_lets.count(let_min):
        let_min = i_let.lower()

print("Количество строк в Дзене Пайтона:", line_count)
print("Количество букв в Дзене Пайтона:", len(text_lets))
print("Количество слов в Дзене Пайтона:", len(text_words))
print("Самая редкая буква в Дзене Пайтона:", let_min)

# зачтено
