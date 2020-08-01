import random
def merge_sort(lst, acsend=True):
    l = len(lst)
    # base case
    if l<=1:
        return lst
    m = l//2
    left = merge_sort(lst[:m]) # from lst[0] to lst[m-1] 
    right = merge_sort(lst[m:]) # from list[m] to lst[-1]

    i,j=0,0
    res = []
    while i<len(left) or j<len(right):
        if i==len(left):
            res.append(right[j])
            j+=1
        elif j==len(right):
            res.append(left[i])
            i+=1
        else:
            if (acsend and left[i]<right[j]) or \
               (not acsend and left[i]>right[j]):
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1

    return res

def merge_sort_bu(a, acsend=True):
    lst = list(a)

    def merge(fs, ss, se):
        i=fs
        j=ss

        s_lst = fs
        while i<ss or j<=se:
            if i<ss and j<=se:
                if ( acsend and aux[i]<aux[j] ) or ( not acsend and aux[i]>aux[j]):
                    lst[s_lst] = aux[i]
                    i+=1
                else:
                    lst[s_lst] = aux[j]
                    j+=1
            elif j>se:
                    lst[s_lst] = aux[i]
                    i+=1
            else:
                    lst[s_lst] = aux[j]
                    j+=1
            s_lst+=1

    l = len(lst)
    left_length=1
    while left_length<l:
        aux = list(lst)
        for j in range(0, l-left_length, left_length*2):
            merge(j, j+left_length, min(j+left_length*2-1, l-1))
        left_length *=2
    return lst

if __name__ == "__main__":
    l=[]
    for j in range(5):
        for i in range(200):        
            l.append(random.randint(0, 1000))
        # print(l)
        assert(merge_sort_bu(l) == merge_sort(l))
