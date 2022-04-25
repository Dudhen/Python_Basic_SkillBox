import timeit

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(res)

result: float = timeit.timeit('"-".join([str(num) for num in range(100)])', number=10000)
print(result)

result_2: float = timeit.timeit('"-".join(map(str, [num for num in range(100)]))', number=10000)
print(result_2)

# зачтено
