def calculating_math_func(data, cache={}):
    if type(cache) == dict:
        cache = cache
    else:
        cache = {}
    if data in cache:
        return cache[data]
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    cache[data] = result
    return calculating_math_func(data)


print(calculating_math_func(5))

# зачтено
