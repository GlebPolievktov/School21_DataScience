class Research(object):
    def file_reader(self):
        with open(file="data.csv",mode="r") as file:
            mass = file.read()
            return mass
        

if __name__ == "__main__":
    obj = Research()
    print(obj.file_reader())