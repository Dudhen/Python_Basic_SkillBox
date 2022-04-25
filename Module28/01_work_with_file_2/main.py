class File:
    def __init__(self, file_name: str, mode: str, encoding="utf8"):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        try:
            file_obj = open(self.file_name, self.mode)
        except FileNotFoundError:
            file_obj = open(self.file_name, "w")
        return file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        return True


with File("text_file.txt", "w") as file:
    file.write("Все работает.\n")

# зачтено
