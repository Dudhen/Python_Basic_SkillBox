zen_file = open("zen.txt", "r")
text = []
for i_line in zen_file:
    text.append(i_line)
for i_line in text[::-1]:
    print(i_line, end="")
zen_file.close()

# зачтено
