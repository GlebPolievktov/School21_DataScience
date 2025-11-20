from random import randint

class Research(object):
    def __init__(self,filename):
        self.filename = filename
    def file_reader(self,has_header = True):
        with open(self.filename,"r") as file:
            r = file.readlines()
        if has_header:
            mass = [i.strip().split(',') for i in r[1:]]
            arr = [[int(s) for s in i] for i in mass]
        else:
            arr = [[int(value) for value in line.strip().split(',')] for line in r]
        for i in arr:
            if len(i) != 2:
                raise ValueError("Incorrect number og header")
        for j in arr:
            if not (0 in j or 1 in j):
                raise ValueError("You should have in one line 0,1 or 1,0")
        return arr
    class Calculations:
        def __init__(self,data):
            self.data = data
        @staticmethod
        def counts(data:list)->tuple[int,int]:
            first = [i[0] for i in data]
            second = [j[1] for j in data]
            return first.count(1),second.count(1)
        @staticmethod
        def fractions(first:int,second:int)->tuple[float,float]:
            summa = first + second
            first_pr = (first/summa)*100
            second_pr = (second/summa)*100
            return first_pr,second_pr
    class Analytics(Calculations):
        def save_file(self,data,filename):
            with open(filename,'w') as file:
                file.write(data)
        def predict_random(self,predict_to_return=5):
            pr = []
            for i in range(predict_to_return):
                j = randint(0,1)
                p = [j,int(not j)]
                pr.append(p)
            return pr
        def predict_last(self):
            return self.data[-1]