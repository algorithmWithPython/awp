def printdp(dp):
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            print('T' if dp[i][j] else "F", end=' ')
        print()

def solution(lst, dp, total):
    res = []
    for i in range(len(lst)):
        if dp[i+1][total-lst[i]]:
            res.append(lst[i])
            total -= lst[i]
    return res

def subset_sum(lst, total):
    l = len(lst)
    dp = [ [False]*(total+1) for _ in range(l+1)] 
    dp[l][0] = True
    for i in range(l-1, -1, -1):
        dp[i][0] = True
        for j in range(1, total+1):
            dp[i][j] = dp[i+1][j]
            if lst[i] <= j:
                dp[i][j] = dp[i][j] or dp[i+1][j-lst[i]]
    printdp(dp)
    print(solution(lst, dp, total))
    return dp[0][total]


lst = [10, 7, 5, 18, 12, 20, 15]
print( subset_sum(lst, 35) )

lst = [15, 22, 14, 26, 32, 9, 16, 8]
print( subset_sum(lst, 53) )

lst = [11, 6, 5, 1, 7, 13, 12]
print( subset_sum(lst, 15) )
        
