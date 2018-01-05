lst = [5, 10, 3, 7, 9, 6, 2, 1, 8, 12]

import copy
lst1 = copy.deepcopy(lst)
print(lst1)

def partition(lst, lo, hi):
    pivot = lst[lo]
    i = lo + 1
    j = hi

    done = False
    while not done:
        while lst[i] <= pivot and i <= j:
            i += 1
        while lst[j] >= pivot and j >= i:
            j -= 1
        if i > j:
            done = True
        else:
            lst[i], lst[j] = lst[j], lst[i]
    lst[lo], lst[j] = lst[j], lst[lo]
    return j

def quicksort(lst, lo, hi):
    if lo < hi:
        p = partition(lst, lo, hi)
        quicksort(lst, lo, p - 1)
        quicksort(lst, p + 1, hi)

quicksort(lst1, 0, len(lst1) - 1)
print(lst1)

lst2 = copy.deepcopy(lst)


def partition2(lst, lo, hi):
    pivot = lst[hi]
    i = lo
    j = hi - 1

    done = False
    while not done:
        while lst[i] <= pivot and i <= j:
            i += 1
        while lst[j] >= pivot and j >= i:
            j -= 1
        if i > j:
            done = True
        else:
            lst[i], lst[j] = lst[j], lst[i]
    lst[hi], lst[i] = lst[i], lst[hi]
    return i

def quicksort2(lst, lo, hi):
    if lo < hi:
        p = partition2(lst, lo, hi)
        quicksort2(lst, lo, p - 1)
        quicksort2(lst, p + 1, hi)

quicksort2(lst2, 0, len(lst2) - 1)
print(lst2)