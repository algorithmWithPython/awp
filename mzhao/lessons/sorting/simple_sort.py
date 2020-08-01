import random
import timeit
import time
def selection_sort(a, acsent=True): # l^2
    lst = list(a)
    l = len(lst)
    for i in range(l): # l
        minmax = i
        for j in range(i+1, l): # l*l
            if (acsent and lst[j]<lst[minmax]) or \
               (not acsent and lst[j]>lst[minmax]):
                minmax = j
        lst[i], lst[minmax] = lst[minmax], lst[i]
    return lst

def insertion_sort(a, acsent=True):
    lst = list(a)
    l = len(lst)
    for i in range(1, l): # l
        v = lst[i]
        j= i
        while j>0 and ((acsent and lst[j-1]>v) or (not acsent and lst[j-1]<v)): # l 
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = v
    return lst

if __name__ == "__main__":
    l=[]
    for i in range(400):
        l.append(random.randint(0, 100000))

    start_time = time.time()
    insertion_sort(l, False)
    finish_time = time.time()
    print(f"insertion run in {finish_time-start_time} seconds")
    print('insertion sort finished')
    start_time = time.time()
    selection_sort(l, False)
    finish_time = time.time()
    print(f"selection run in {finish_time-start_time} seconds")
    print('selection sort finished')
    assert(sorted(l, reverse=True) == insertion_sort(l, False))
    assert(selection_sort(l, False) == insertion_sort(l, False)) 
