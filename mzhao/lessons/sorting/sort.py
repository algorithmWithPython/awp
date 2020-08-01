import timeit
import random
import shell_sort

def selection_sort(b):
    a=list(b)
    l = len(a)
    for i in range(l-1):
        m = i
        for j in range(i+1, l):
            if a[j]<a[m]:
                m=j
        if m != i:
            a[i], a[m] = a[m], a[i]
    return a

def insertion_sort(b):
    a = list(b)
    l = len(a)
    for i in range(1, l):
        j=i
        v=a[i]
        while j>=1 and v<a[j-1]:
            a[j] = a[j-1]
            j-=1
        a[j]=v
        # j=i
        # while j>0 and a[j-1]>a[j]:
        #     a[j], a[j-1] = a[j-1], a[j]
        #     j-=1
    return a

if __name__ == "__main__":
    # verify shell sort
    for i in range(5):
        l = []                 
        for i in range(200):
            l.append(random.randint(-100000, 100000))
        i_s = insertion_sort(l)
        s_s = selection_sort(l)
        # shell = shell_sort.shell_sort(l)
        assert( i_s == s_s )
        #assert( i_s == shell )
    num = 2000

    setup = '''import random
import shell_sort
import sort'''

    selection = f'''
l = []
for i in range({num}):
    l.append(random.randint(-100000, 100000))
sort.selection_sort(l)'''

    insertion = f'''
l = []
for i in range({num}):
    l.append(random.randint(-100000, 100000))
sort.insertion_sort(l)'''

    print("sel_s", timeit.repeat(stmt=selection, setup=setup, number=1, repeat=3))
    print("ins_s", timeit.repeat(stmt=insertion, setup=setup, number=1, repeat=3))

    shell = f'''
l = []
for i in range({num}):
    l.append(random.randint(-100000, 100000))
shell_sort.shell_sort(l)'''
    print("shell", timeit.repeat(stmt=shell, setup=setup, number=1, repeat=3))
