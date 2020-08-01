# test the performance of insertion sort, selection sort
# merge sort and quick sort

# this requires simple_sort.py, quick_sort.py and merge_sort.py
# to be in the same directory of this file.

import timeit
'''
def qs():
    l = []
    for i in range(20000):
        l.append(random.randint(-1000, 1000))
    return quick_sort.QuickSort(l, False).sort()

def insert():
    l = []
    for i in range(20000):
        l.append(random.randint(-1000, 1000))
    res = insertion_sort(l, False)

def select():
    l = []
    for i in range(20000):
        l.append(random.randint(-1000, 1000))
    res = selection_sort(l, False)
'''

num = 2000 # to 3200 
qs_code=f'''
def qs():
    l = []
    for i in range({num}):
        l.append(random.randint(-1000, 1000))
    return quick_sort.QuickSort(l, False).sort()
qs()
'''

ms_code=f'''
def ms():
    l = []
    for i in range({num}):
        l.append(random.randint(-1000, 1000))
    return merge_sort.merge_sort_bu(l, False).sort()
ms()
'''

is_code=f'''
def insert():
    l = []
    for i in range({num}):
        l.append(random.randint(-1000, 1000))
    res = simple_sort.insertion_sort(l, False)
insert()
'''

ss_code=f'''
def select():
    l = []
    for i in range({num}):
        l.append(random.randint(-1000, 1000))
    res = simple_sort.selection_sort(l, False)
select()
'''

setup='''
import random
import quick_sort
import simple_sort
import merge_sort
''' 

print("qs", timeit.repeat(stmt=qs_code, setup=setup, number=2, repeat=3))
print("is", timeit.repeat(stmt=is_code, setup=setup, number=2, repeat=3))
print("ss", timeit.repeat(stmt=ss_code, setup=setup, number=2, repeat=3))
print("ms", timeit.repeat(stmt=ms_code, setup=setup, number=2, repeat=3))
