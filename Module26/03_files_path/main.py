import os


def gen_files_path(catalog: str, path=r"C:"):
    for i_elem in os.listdir(path):
        object_way = os.path.join(path, i_elem)
        if i_elem != catalog and os.path.isfile(object_way):
            yield object_way
        elif i_elem != catalog and os.path.isdir(object_way):
            my_generator_2 = gen_files_path(catalog, object_way)
            for i_val in my_generator_2:
                yield i_val
        elif i_elem == catalog:
            yield object_way + "\nУказанный файл найден!"


way = "../../Module19"

my_generator = gen_files_path("07_pizza", way)

for i_value in my_generator:
    print(i_value)
    if "Указанный файл найден!" in i_value:
        break

# зачтено
