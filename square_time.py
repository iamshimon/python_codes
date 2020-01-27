import timeit

def f1():
    sq = [x**2 for x in range(1,20)]
    return sq

def f2():
    s=1
    while s<21:
        yield s**2
        s+=1

print(timeit.Timer(f1).timeit(number=100000))
print(timeit.Timer(f2).timeit(number=100000))