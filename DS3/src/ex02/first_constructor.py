import sys
class Research(object):
    def __init__(self,file_txt):
        self.file_txt = file_txt
    def file_reader(self):
        with open(self.file_txt,"r") as file:
            mass = file.read()
        arr1 = mass.split('\n')
        if len(arr1[0].split(',')) != 2:
            raise ValueError("Incorrect number og header")
        for i in range(1,len(arr1)):
            if arr1[i] != '0,1' and arr1[i] != '1,0':
                raise ValueError("You should have in one line 0,1 or 1,0")
        return mass


if __name__ == "__main__":
    if len(sys.argv[:]) != 3:
        obj = Research(sys.argv[1])
        print(obj.file_reader())
    else:
        raise ValueError("You should write python3 file.py file.csv")