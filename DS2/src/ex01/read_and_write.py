def read_and_write(filename_csv:str,filename_tsv:str):
    with open(filename_csv,"r") as file_csv:
        with open(filename_tsv,"w") as file_tsv:
            a = file_csv.read().replace("','",'"\t"').replace('",','"\t"').replace('false,','false\t').replace('true,','false\t')
                                         
            cont = file_tsv.write(a)
if __name__ == "__main__":
    read_and_write("ds.csv","ds.tsv")