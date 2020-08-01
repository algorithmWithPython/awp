#https://www.hackerearth.com/zh/practice/algorithms/sorting/selection-sort/practice-problems/algorithm/old-keypad-in-a-foreign-land-24/description/

n = int(input())
frequencies = list(map(int, input().split()))
k = int(input())
keySize = list(map(int, input().split()))
frequencies = sorted(frequencies, reverse=True)
keySize = sorted(keySize)
answer = 0
index = 1
total = sum(keySize)

if total < n:
    print(-1)
else:
    x = 0
    for i in range(n):
        for j in range(k):
            if x < n :
                if keySize[j]>0:
                    keySize[j] -= 1
                    answer += index*frequencies[x]
                    x += 1
        index += 1
    print(answer)	
