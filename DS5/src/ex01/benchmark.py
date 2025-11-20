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
def func3(email:list)->list:
    return list(map(lambda i : i if i.endswith('@gmail.com') else None,email))

if __name__ == "__main__":
    execution_time1 = timeit.timeit(lambda: func1(emails), number=90000)
    execution_time2 = timeit.timeit(lambda: func2(emails), number=90000)
    execution_time3 = timeit.timeit(lambda: func3(emails), number=90000)
    j = ['a simple loop','a list comprehension','a map']
    if execution_time1 < execution_time2 and execution_time1 < execution_time3:
        print(f'it is better to use {j[0]}')
    elif execution_time2 < execution_time1 and execution_time2 < execution_time3:
        print(f'it is better to use {j[1]}')
    elif execution_time3 < execution_time1 and execution_time3 < execution_time2:
        print(f'it is better to use {j[2]}')
    total = [execution_time1,execution_time2,execution_time3]
    tot = sorted(total)
    over = str(tot[0]) + " vs " + str(tot[1]) + " vs " + str(tot[2])
    print(over)
    




