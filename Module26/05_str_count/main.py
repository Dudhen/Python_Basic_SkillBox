import os


def my_func(my_way: str):
    indexs_files = []
    q = 0
    for i_elem in os.listdir(my_way):
        object_way = os.path.join(way, i_elem)
        if not i_elem.endswith(".py") and os.path.isfile(object_way):
            indexs_files.append(q)
        q += 1
    return indexs_files


def code_str_count(path: str):
    str_count = 0
    for i_elem in os.listdir(path):
        object_way = os.path.join(path, i_elem)
        if os.path.isfile(object_way) and i_elem.endswith(".py"):
            count_str = 0
            file = open(object_way, "r", encoding="utf8")
            for i_line in file:
                let_count = 0
                lets_list = []
                for i_let in i_line:
                    let_count += 1
                    lets_list.append(i_let)
                if let_count != 1 and lets_list[0] != "#":
                    count_str += 1
            file.close()
            str_count += count_str
        elif os.path.isdir(object_way):
            str_count = 0
            for i_value in code_str_count(object_way):
                str_count = i_value
        yield str_count


way = "../../Module19/02_geography"

my_generator = code_str_count(way)
i = 0
str_count = 0

my_list = my_func(way)

for i_value in my_generator:
    good = False
    is_file = False
    for i_elem in os.listdir(way):
        object_way = os.path.join(way, i_elem)
        if os.path.isfile(object_way):
            is_file = True
            if i not in my_list:
                good = True
    if is_file:
        if good:
            str_count += i_value
    else:
        str_count += i_value
    i += 1

print("\nВ питоновских файлах директории "
      "по указанному пути обнаружено {} строк кода\n(Без учета пустых строк и комментариев)".format(str_count))

# зачтено
