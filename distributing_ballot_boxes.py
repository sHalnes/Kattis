import sys
from math import ceil, floor
#import queue as Q

for case in range(3):
    data = sys.stdin.readline().split()
    if data[0] == data[1] == '-1':
        exit()
    n_cities = int(data[0])
    n_boxes = int(data[1])

    if n_cities == n_boxes:
        maximum = 0
        for i in range(n_cities):
            citizens = sys.stdin.readline()
            if int(citizens) > maximum:
                maximum = int(citizens)
        print(maximum)
    elif n_cities == 1:
        citizens = sys.stdin.readline()
        maxi = int(citizens)/n_boxes
        if type(maxi) is float and int(maxi) < maxi:
            maxi = int(maxi) + 1
        else:
            maxi = int(maxi)
        print(maxi)
    else:

        population = []
        max_citizens = 0
        for i in range(n_cities):
            citizens = int(sys.stdin.readline())
            population.append(citizens)
            if citizens > max_citizens:
                max_citizens = citizens
        def binary_search(lo, hi):
            while lo+1 < hi:
                middle = (lo+hi)//2
                boxes_used = 0
                for i in population:
                    boxes_used += ceil(i/middle)
                if boxes_used > n_boxes:
                    lo = middle
                if boxes_used <= n_boxes:
                    hi = middle
            return hi
        max_boxes = binary_search(0, max_citizens)
        print(max_boxes)
    blank_line = sys.stdin.readline()