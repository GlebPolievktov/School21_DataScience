#!/usr/bin/env python3
import timeit
import sys

emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 
'anna@live.com', 'philipp@gmail.com'] * 5
def func1(emails:list)->list:
    a = []
    for i in emails:
        if i.endswith('@gmail.com'):
            a.append(i)
    return a

def func2(emails:list)->list:
    return [i for i in emails if i.endswith('@gmail.com')]
def func3(email:list)->list:
    return list(map(lambda i : i if i.endswith('@gmail.com') else None,email))
def func4(email:list)->list:
    return list(filter(lambda i : i if i.endswith('@gmail.com') else None,email))


if __name__ == "__main__": 
    if len(sys.argv) != 3:
        sys.exit(0)
    
    type_of_func = sys.argv[1]
    iterations = int(sys.argv[2])
    
    if type_of_func == 'loop':
        execution_time1 = timeit.timeit(lambda: func1(emails), number=iterations)
        print(execution_time1)
    elif type_of_func == 'list_comprehension':
        execution_time2 = timeit.timeit(lambda: func2(emails), number=iterations)
        print(execution_time2)
    elif type_of_func == 'map':
        execution_time3 = timeit.timeit(lambda: func3(emails), number=iterations)
        print(execution_time3)
    elif type_of_func == 'filter':
        execution_time4 = timeit.timeit(lambda: func4(emails), number=iterations)
        print(execution_time4)
    else:
        print("Unknown function type")

        

    
    
    