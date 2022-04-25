import re

numbers = ['9999999999', '999999-999', '99999x9999']

i = 1
for i_numb in numbers:
    print("{} номер:".format(i), end=" ")
    result = re.match(r"[8, 9]", i_numb)
    res = re.findall(r'\d+', i_numb)
    if result and res[0] == i_numb and len(i_numb) == 10:
        print("все в порядке")
    else:
        print("не подходит")
    i += 1

# зачтено
