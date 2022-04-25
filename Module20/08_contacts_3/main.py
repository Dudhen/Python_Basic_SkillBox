def add_contact(dictBook):
    surname_name = input("Введите фамилию и имя контакта через пробел в формате ФИ\n: ").split()
    number = int(input("Введите номер телефона абонента\n: "))
    if tuple(surname_name) in dictBook.keys():
        print("Этот человек уже имеется в ваших контактах!")
    else:
        dictBook[tuple(surname_name)] = number
    print("\nСписок ваших контактов:")
    for i_key, i_value in dictBook.items():
        for i_name in i_key:
            print(i_name, end=" ")
        print(i_value)
    print()


def search(dictBook):
    surname = input("Введите фамилию: ").title()
    print()
    for i_name, i_numb in dictBook.items():
        if surname in i_name or surname + "а" in i_name or surname[:-1] in i_name:
            print(i_name[0], i_name[1], i_numb)
    print()


def process(dictBook):
    question = input("Какое действие вы бы хотели совершить?\n(\"Добавить контакт\", \"Поиск по фамилии\")\n: ").lower()
    if question == "добавить контакт":
        add_contact(dictBook)
    elif question == "поиск по фамилии":
        search(dictBook)
    else:
        print("Ошибка ввода! Введите одну из двух вышеперечисленных команд")
    process(dictBook)


phonebook = {
    ("Дудченко", "Арсений"): 89891775401,
    ("Иванов", "Илья"): 89907563723,
    ("Иванова", "Анна"): 89907563723,
    ("Степанов", "Василий"): 89784632756
}

process(phonebook)

# зачтено
