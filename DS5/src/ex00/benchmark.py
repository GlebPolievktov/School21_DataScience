import timeit

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

if __name__ == "__main__":
    execution_time1 = timeit.timeit(lambda: func1(emails), number=9000)
    execution_time2 = timeit.timeit(lambda: func2(emails), number=9000)
    j = ['a simple loop','list comprehension']
    if execution_time1 < execution_time2:
        print(f'it is better to use {j[0]}')
        print(f'{execution_time1} vs {execution_time2}')
    else:
        print(f'it is better to use {j[1]}')
        print(f'{execution_time2} vs {execution_time1}')


