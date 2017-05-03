import csv
from linked_list import *


def read_csv(filename):
    with open("C:/Users/100579259/Documents/GitHub/ConvexHull/convex_hull/"+filename, 'rb') as f:
        reader = csv.reader(f)
        file_list = list(reader)

    del file_list[0]

    point_list = LinkedList()
    for b in file_list:
        point_list.append(Point(float(b[0]), float(b[1])))

    return point_list


