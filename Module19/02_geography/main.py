countryCount = int(input("Кол-во стран: "))

citysInCountrys = dict()

for i_country in range(countryCount):
    print(i_country + 1, "страна: ", end="")
    country = input().split()
    citysInCountrys[country[0]] = country[1:]

for search in range(3):
    print()
    print(search + 1, "город: ", end="")
    city = input()
    i = 1
    for country in citysInCountrys:
        if city in citysInCountrys[country]:
            print("Город", city, "расположен в стране", country)
            break
        elif i == countryCount:
            print("По городу", city, "данных нет")
        i += 1

# зачтено
