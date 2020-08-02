import sys
def lis(lst, i, j):
    if j == len(lst):
        return 0
    if lst[i]>=lst[j]:
        return lis(lst, i, j+1)
    else:
        return max(lis(lst, i, j+1), lis(lst, j, j+1)+1)

#i = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 7]
#i= [10,9,2,5,3,7,101,18]
i= [10, 22, 9, 33, 21, 50, 41, 60, 80]
i.insert(0, -sys.maxsize)
print(lis(i, 0, 1))


        