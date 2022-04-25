def zipReplica(iter_1, iter_2):
    minLen = 0
    if len(iter_1) <= len(iter_2):
        minLen = len(iter_1)
    else:
        minLen = len(iter_2)
    result = ((iter_1[i], iter_2[i]) for i in range(minLen))
    return result


iterator_1 = 'abcd'
iterator_2 = (10, 20, 30, 40, 50)

print("\nРезультат:")
result = zipReplica(iterator_1, iterator_2)
print(result)
for i_pair in result:
    print(i_pair)

# зачтено
