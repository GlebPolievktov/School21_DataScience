class Must_Read(object):
    with open(file="data.csv",mode="r") as file:
        print(file.read())

if __name__ == "__main__":
    Must_Read()