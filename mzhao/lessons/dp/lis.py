import sys
def print_mem(mem):
    width = 3
    for i in range(len(mem)):
        for j in range(len(mem[0])):
            print(f'{mem[i][j]:<{width}}', end=' ')
        print()

def chosen(mem):
    l = len(mem)
    res = []
    for i in range(l-1, 0, -1):
        if mem[0][i] != mem[0][i-1]:
            res.append(lst[i])
    return res

def chosen1(mem):
    l = len(mem)
    res = []
    for i in range(l-1, 0, -1):
        if mem[0][i] != mem[0][i-1]:
            res.append(lst[i])
    return res

def lis(lst): # O(n^2), O(n^2)
    lst.insert(0, -sys.maxsize)
    l = len(lst)
    mem = [[1]*(l+1) for _ in range(l)]

    for i in range(l-2, -1, -1):
        for j in range(l-1, i, -1):
            if lst[i]>=lst[j]:
                mem[i][j] = mem[i][j+1]
            else:
                mem[i][j] = max(mem[i][j+1], mem[j][j+1]+1)
    print_mem(mem)
    #print(chosen(mem))
    return mem[0][1]-1

def lis1(lst): # O(n^2), O(n)
    lst.insert(0, -sys.maxsize)
    l = len(lst)
    mem = [1]*l
    for i in range(l-2, -1, -1):
        best = 1
        for j in range(i+1, l):
            if lst[j]>lst[i]:
                best = max(best, mem[j]+1)
        mem[i]=best
    print(mem)
    print(chosen1(mem))
    return mem[1]


lst= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#lst = [10, 22, 9, 33, 21, 50, 41, 60, 80] # 10, 22, 33, 50, 60, 80
#lst = [10, 22, 9, 33, 21, 50, 41, 60, 80, 61] # 10, 22, 33, 50, 60, 80

print(lis(lst))