# basically try to think what kind of box can be put into the same box at the end.
# 
# for example:
#  1 2 2 3 3 3 4 4 5 6 6 6 6 7 7 8
# 
# can be view as following
# 
# 1
# 2 2
# 3 3 3
# 4 4
# 5
# 6 6 6 6 
# 7 7
# 8


tc = int(input())
for _ in range(tc):
    num = int(input())
    lst = []
    d = {}
    res = 0
    for _ in range(num):
        v = int(input())
        d.setdefault(v, 0)
        d[v]+=1
        if d[v]>res:
            res=d[v]
    print(res)