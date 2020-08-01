t = int(input())
n = int(input())
chores = list(map(int, input().split()))
chores.sort()

res = 0
for i in chores:
    if chores[i]<=t:
        t -= chores[i]
        res += 1
    else:
        break

print(res)