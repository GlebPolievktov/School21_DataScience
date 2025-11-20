from analytics import Research
from config import *

if __name__ == "__main__":
    r = Research(filename=file)
    arr = r.file_reader(has_header=True)
    m = Research.Analytics(data=arr)
    m1,m2 = m.counts(data=arr)
    n1,n2 = m.fractions(m1,m2)
    h = Research.Analytics(data=arr).predict_random()
    p1 = [i[0] for i in h]
    p2 = [j[1] for j in h]
    p1 = p1.count(1)
    p2 = p2.count(1)
    total = report.format(
        m1+m2,
        m1,
        m2,
        n1,
        n2,
        len(h),
        p1,
        p2
    )
    m.save_file(total,"report.txt")
    