import re

numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

pattern_1 = r'\b\w\D{1}\d{5,6}'
pattern_2 = r'\b\w\D{0}\d{3}\w\D\d{2,3}'

result = re.findall(pattern_2, numbers)

print("Список номеров частных автомобилей: {}".format(result))

result = re.findall(pattern_1, numbers)

print("Список номеров такси: {}".format(result))

# зачтено