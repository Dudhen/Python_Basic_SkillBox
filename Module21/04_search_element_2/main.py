def key_in_dict(dict_1, key, depth):
    if not key in dict_1.keys():
        if depth != 1:
            for i_key in dict_1.keys():
                if isinstance(dict_1[i_key], dict):
                    if key_in_dict(dict_1[i_key], key, depth - 1):
                        return True
    else:
        print(dict_1[key])
        return True


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key_word = input("Введите искомый ключ: ")

question = input("Хотите указать максимальную глубину поиска? (\"да\"\\\"нет\"): ").lower()

if question == "да":
    depth = int(input("Введите максимальную глубину поиска: "))
    question = depth
else:
    question = -1

if key_in_dict(site, key_word, question) == None:
    print("На заданной глубине ключа не найдено или его в принципе нет.")

# зачтено
