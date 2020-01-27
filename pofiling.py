import cProfile

def f1():
    sq = [x**2 for x in range(1,200000)]
    return sq

def f2():
    s=1
    while s<200001:
        yield s**2
        s+=1

print(cProfile.runctx("f1()",globals(),locals()))

print(cProfile.runctx("f2()",globals(),locals()))