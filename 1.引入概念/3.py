from timeit import Timer

def test1():
    li  = []
    for i in range(1001):
        li.append(i)

def test2():
    li = []
    for i in range(1001):
        li = li + [i]

def test3():
    li = [i for i in range(1001)]

def test4():
    li = list(range(1001))

def test5():
    li = []
    for i in range(1001):
        li.insert(0, i)

def test6():
    li = []
    for i in range(1001):
        li += [i]

def test7():
    li = []
    for i in range(1001):
        li.extend([i])

timer1 = Timer("test1()", "from __main__ import test1")
print("append", timer1.timeit(number=1000))
timer2 = Timer("test2()", "from __main__ import test2")
print("li = li + i", timer2.timeit(number=1000))
timer3 = Timer("test3()", "from __main__ import test3")
print("[i for in range()]", timer3.timeit(number=1000))
timer4 = Timer("test4()", "from __main__ import test4")
print("list(range())", timer4.timeit(number=1000))
timer5 = Timer("test5()", "from __main__ import test5")
print("insert", timer5.timeit(number=1000))
timer6 = Timer("test6()", "from __main__ import test6")
print("+=", timer6.timeit(number=1000))
timer7 = Timer("test7()", "from __main__ import test7")
print("extend", timer7.timeit(number=1000))



