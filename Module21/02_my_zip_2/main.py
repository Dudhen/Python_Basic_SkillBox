def zipReplica_2(iter_1, iter_2):
    minLen = min(len(iter_1), len(iter_2))
    result = ((iter_1[i], iter_2[i]) for i in range(minLen))
    return result


iterator_1 = 'abcd'
iterator_2 = (10, 20, 30, 40, 50)
for i in zipReplica_2(iterator_1, iterator_2):
    print(i)

# зачтено
