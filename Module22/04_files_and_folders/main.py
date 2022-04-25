import os


def getFolderSize(folder):
    total_size = os.path.getsize(folder)
    total_files = 0
    for item in os.listdir(folder):
        itempath = os.path.join(folder, item)
        if os.path.isfile(itempath):
            total_files += 1
            total_size += os.path.getsize(itempath)
        elif os.path.isdir(itempath):
            total_size += getFolderSize(itempath)
    return total_size, total_files


way = r"C:\Users\1\PycharmProjects\Python_Basic\Module19"

size = 0
files_count = 0
dir_count = 0

for i_elem in os.listdir(way):
    object_way = os.path.join(way, i_elem)
    if os.path.isfile(object_way):
        files_count += 1
        size += os.path.getsize(object_way)
    elif os.path.isdir(object_way):
        dir_count += 1
        size += getFolderSize(object_way)[0]
        files_count += getFolderSize(object_way)[1]

print("Размер каталога (в Кб):", size / 1024)
print("Количество подкаталогов:", dir_count)
print("Количество файлов:", files_count)

# зачтено
