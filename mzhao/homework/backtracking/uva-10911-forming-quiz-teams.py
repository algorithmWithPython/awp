import math
import sys
import time
count = 1
while True:
    n = int(input())*2
    if n == 0:
        break
    s = []
    v = [0]*n
    res = sys.maxsize
    def distance(i, j):
        return math.hypot(s[i][0]-s[j][0], s[i][1]-s[j][1])

    for i in range(n):
        name, x, y = input().split()
        s.append((int(x), int(y)))

    d = [ [0]*n for _ in range(n) ]
    for i in range(n-1):
        for j in range(i+1, n):
            d[i][j] = distance(i, j)

    def dfs(i, total_dis):
        global res
        # if total_dis > res:
        #     return
        if i == n:
            if total_dis < res:
                res = total_dis
            return
        if v[i] == 1:
            dfs(i+1, total_dis)
        else:
            v[i]=1
            for j in range(i+1, n):
                if v[j]==0:
                    v[j]=1
                    dfs(i+1, total_dis+d[i][j])
                    v[j]=0
            v[i]=0
    start = time.time()
    dfs(0, 0)
    print(f"Case {count}: {res:.2f}")
    count+=1
    