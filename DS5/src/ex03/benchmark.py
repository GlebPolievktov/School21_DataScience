#!/usr/bin/env python3
import timeit
from functools import reduce
import sys

def add(x:int,y:int)->int:
    return x + y
def func1(dig:int)->int:
    sum = 0
    for i in range(1,dig+1):
        sum = sum + i*i
    return sum

def func2(dig:int)->int:
    list1 = [i**2 for i in range(1,dig+1)]
    res = reduce(add,list1)
    return res

if __name__ == "__main__": 
    if len(sys.argv) != 4:
        sys.exit(0)
    
    type_of_func = sys.argv[1]
    iterations = int(sys.argv[2])
    digit = int(sys.argv[3])
    
    if type_of_func == 'loop':
        execution_time1 = timeit.timeit(lambda: func1(digit), number=iterations)
        print(execution_time1)
    elif type_of_func == 'reduce':
        execution_time2 = timeit.timeit(lambda: func2(digit), number=iterations)
        print(execution_time2)
    else:
        print("Unknown function type")
    
    