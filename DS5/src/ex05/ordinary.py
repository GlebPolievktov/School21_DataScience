#!/usr/bin/env python3
import resource
import sys
import time

def file_to_read():
    file = sys.argv[1]
    with open(file,"r") as f:
        j = f.readlines()
    return j

if __name__ == "__main__":
    beg = time.time()
    h = file_to_read()
    for i in h:
        pass
    end = time.time()
    print(f'User Mode Time + System Mode Time = {end-beg:.2f}s')
    memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    print(f'Peak Memory Usage = {memory/(1024*1024)} GB')