import sys
def lis(lst, prev_idx, curr_idx):
    if curr_idx == len(lst):
        return 1
    if lst[curr_idx] <= lst[prev_idx]:
        return lis(lst, prev_idx, curr_idx+1)
    
    skip = lis(lst, prev_idx, curr_idx+1)
    take = lis(lst, curr_idx, curr_idx+1)+1
    return max(skip, take)

lst = [10, 22, 9, 33, 21, 50, 41, 60, 80] # 10, 22, 33, 50, 60, 80
# lst = [50, 3, 10, 7, 40, 80] # 3, 7, 40, 80
# lst = [3,10, 2, 1, 20] # 3, 10, 20
# lst = [0] # 0
lst.insert(0, -sys.maxsize)
print(lis(lst, 0, 1)-1)

