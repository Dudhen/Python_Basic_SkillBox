site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def site_created(siteCount, site):
    if siteCount != 0:
        product = input("Введите название продукта для нового сайта: ")
        site["html"]["head"]["title"] = "Куплю/продам {} недорого".format(product)
        site["html"]["body"]["h2"] = "У нас самая низкая цена на {}".format(product)
        print("Сайт для", product + ":")
        print("site = ", site)
        site_created(siteCount - 1, site)


siteCount = int(input("Сколько будет сайтов?: "))

site_created(siteCount, site)

# зачтено

# Но вообще, здесь надо было сделать рекурсивную фукнцию, которая обходила вебс макет
# и менял в нужный ключах значения. Например так бы выглядел вызов:
# find_and_replace(copy_site=copy_site, key='title', value="Куплю/продам {} недорого".format(product))
# find_and_replace(copy_site=copy_site, key='h2', value="У нас самая низкая цена на {}".format(product))
# А вовзращался бы изменненый макет
