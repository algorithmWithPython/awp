def mostFreqent(a, limit):
    biggest = max([x for x in a if x < limit])
    res = []
    for i in range(len(a)):
        if a[i]==biggest:
            res.append(i)
    return res, biggest

n = int(input())
a = [0]*1001
for i in range(n):
    num = int(input())
    a[num]+=1
l,biggest = mostFreqent(a, 2000000)

if len(l)>1:
    print(max(l)-min(l))
else:
    l=l[0]
    sl, sec_biggest = mostFreqent(a, biggest)

    min_sl = min(sl)
    max_sl = max(sl)
    if l<min_sl:
        print(max_sl-l)
    elif l>max_sl:
        print(l-min_sl)
    else:
        print(max(l-min_sl, max_sl-l))
