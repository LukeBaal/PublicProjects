# Quick sort with custom partitioning
def ccw(p1, p2, p3):
    orientation = (p2.get_x() - p1.get_x())*(p3.get_y() - p1.get_y()) - \
                  (p3.get_x() - p1.get_x())*(p2.get_y() - p1.get_y())
    if orientation > 0:  # If ccw, return 1
        return 1
    elif orientation < 0:  # If cw, return -1
        return -1
    else:  # If collinear, return 0
        return 0


# Quick sort the given list
def qsort(a, lo, hi, base):
    if lo < hi:
        p = partition(a, lo, hi, base)
        qsort(a, lo, p-1, base)
        qsort(a, p+1, hi, base)

    return a


# Partition the given sub-list by swapping points base on pivot.
def partition(b, lo, hi, base):
    pivot = b.get(hi)
    i = lo
    for j in range(lo, hi):
        if ccw(base, pivot, b.get(j)) != 1:  # Rather then comparing values, compare cw vs. ccw turn
            b.swap(b.get(i), b.get(j))
            i += 1
    b.swap(b.get(i), b.get(hi))
    return i


