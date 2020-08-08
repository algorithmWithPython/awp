def subset(lst, i, cur_sum):
    if cur_sum == 0:
        return []
    
    if cur_sum < 0 or i==len(lst):
        return None

    include = subset(lst, i+1, cur_sum-lst[i])
    if include != None:
        include.append(lst[i])
        return include

    exclude = subset(lst, i+1, cur_sum)
    if exclude != None:
        return exclude

    return None

lst = [10, 7, 5, 18, 12, 20, 15]
print( subset(lst, 0, 35) )

lst = [15, 22, 14, 26, 32, 9, 16, 8]
print( subset(lst, 0, 53) )

lst = [11, 6, 5, 1, 7, 13, 12]
print( subset(lst, 0, 15) )