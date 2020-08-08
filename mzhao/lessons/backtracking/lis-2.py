import sys
def lis(lst, curr_p):
    best = 1
    for i in range(curr_p+1, len(lst)):
        if lst[i]>lst[curr_p]:
            best = max(best, lis(lst, i)+1)
    return best

# lst = [10, 22, 9, 33, 21, 50, 41, 60, 80] # 10, 22, 33, 50, 60, 80
# lst = [50, 3, 10, 7, 40, 80] # 3, 7, 40, 80
lst = [3,10, 2, 1, 20] # 3, 10, 20
# lst = [0] # 0
lst.insert(0, -sys.maxsize)
print(lis(lst, 0)-1)
