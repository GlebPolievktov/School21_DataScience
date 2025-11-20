def data_types():
    t = tuple('1')
    s = set()
    list_different_data_type = [312,'5',3.14,True,[0,4,2],{'apple':3,'banana':4},t,s]
    mn = "["
    for i in list_different_data_type:
        if (type(i).__name__ == 'set'):
            mn = mn + type(i).__name__ + ""
        else:
            mn = mn + type(i).__name__ + " "
        
    mn+="]"
    print(mn)

if __name__ == "__main__":
    data_types()

