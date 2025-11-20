#!/usr/bin/env python3
import timeit
import random
from collections import Counter
import sys

def func1(iter:int)->list:
    return [random.randint(1,101) for i in range(iter)]
def func2(list1:list)->dict:
    d = dict()
    for i in list1:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d
def func3(list1:list)->dict:
    a = func2(list1=list1)
    return dict(sorted(a.items(),key=lambda x :x[1],reverse=True)[:10])
def func4(list1:list):
    Counter(list1)
def func5(list1:list):
    Counter(list1).most_common(10)

if __name__ == "__main__": 
    execution_time1 = timeit.timeit(lambda: func1(1000000), number=1)
    main_func = func1(1000000)
    execution_time2 = timeit.timeit(lambda: func2(main_func), number=1)
    print(f'my function: {execution_time2}')
    execution_time4 = timeit.timeit(lambda: func4(main_func), number=1)
    print(f'Counter: {execution_time4}')
    execution_time3 = timeit.timeit(lambda: func3(main_func), number=1)
    print(f'my top: {execution_time3}')
    execution_time5 = timeit.timeit(lambda: func5(main_func), number=1)
    print(f"Counter's top: {execution_time5}")

    
