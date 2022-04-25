import random


def one_day():
    exceptions = ["KillError",
                  "DrunkError",
                  "CarCrashError",
                  "GluttonyError",
                  "DepressionError"]

    numb = random.randint(1, 10)
    if numb == 6:
        excep = random.choice(exceptions)
        try:
            raise Exception(excep)
        except Exception:
            with open("karma.log", "a", encoding="utf8") as file:
                file.write("{}\n".format(excep))
    return random.randint(1, 7)


days = 0
karma_summ = 0

while True:
    karma_summ += one_day()
    if karma_summ >= 500:
        break
    days += 1

print("Вы достигли карму в {} очков за {} дней.".format(karma_summ, days))

# зачтено
