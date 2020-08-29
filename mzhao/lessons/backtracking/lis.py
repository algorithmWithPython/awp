import sys
import timeit

def lis(lst, i, j):
    if j == len(lst):
        return 0
    if lst[i]>=lst[j]:
        return lis(lst, i, j+1)
    else:
        return max(lis(lst, i, j+1), lis(lst, j, j+1)+1)

def lis1(lst, i, j, mem):
    if j == len(lst):
        return 0
    if mem[i][j] != -1:
        return mem[i][j]
    if lst[i]>=lst[j]:
        mem[i][j] = lis1(lst, i, j+1, mem)
    else:
        mem[i][j] = max(lis1(lst, i, j+1, mem), lis1(lst, j, j+1, mem)+1)
    return mem[i][j]

if __name__ == "__main__":
    #i = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 7]
    #i= [10,9,2,5,3,7,101,18]
    # i= [10, 22, 9, 33, 21, 50, 41, 60, 80]
    i= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    i.insert(0, -sys.maxsize)
    mem = [[-1]*len(i) for _ in range(len(i))]
    print(lis1(i, 0, 1, mem))

    print(lis(i, 0, 1))
    
    setup = '''
import lis
import sys
i= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

sys.setrecursionlimit(15000)
i.insert(0, -sys.maxsize)
    '''

    s1 = '''
lis.lis(i, 0, 1)-1
    '''

    s2 = '''
mem = [[-1]*len(i) for _ in range(len(i))]
lis.lis1(i, 0, 1, mem)-1
    '''

    print("lis:", timeit.repeat(stmt=s1, setup=setup, repeat=2, number=1))
    print("lis1:", timeit.repeat(stmt=s2, setup=setup, repeat=2, number=1))