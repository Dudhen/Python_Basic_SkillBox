import datetime


class Date:
    @classmethod
    def from_string(cls, string: str):
        str_list = string.split("-")
        result = "День: {}\t\tМесяц: {}\t\tГод: {}".format(str_list[0], str_list[1], str_list[2])
        return result

    @classmethod
    def is_date_valid(cls, string: str):
        str_list = string.split("-")
        years, month, day = int(str_list[2]), int(str_list[1]), int(str_list[0])
        try:
            date = datetime.datetime(years, month, day)
            return True
        except ValueError:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# зачтено
