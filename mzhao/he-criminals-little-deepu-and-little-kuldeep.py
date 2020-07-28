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
