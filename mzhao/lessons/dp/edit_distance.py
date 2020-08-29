# https://leetcode.com/problems/edit-distance/
from pprint import pprint

def solution(dp, a, b):
    r = len(dp)-1
    c = len(dp[0])-1

    string_len = max(len(a), len(b))
    res = []
    res.append(f'orignial strings, \na is {a:>{string_len}}, \nb is {b:>{string_len}}')
    while True:
        if r==0 and c==0:
            break
        elif dp[r][c] == dp[r-1][c]+1:
            insert = a[r-1]
            b = b[:c] + insert + b[c:]
            res.append(f'insert {insert} in b, \na is {a:>{string_len}}, \nb is {b:>{string_len}}')
            r-=1
        elif dp[r][c] == dp[r][c-1]+1:
            print(f'b[c-1]: {c-1}')
            delete = b[c-1]
            b = b[:c-1] + b[c:]
            res.append(f'delete {delete} in b, \na is {a:>{string_len}}, \nb is {b:>{string_len}}')
            c-=1
        elif dp[r][c] == dp[r-1][c-1]+1:
            replaced = a[r-1]
            replace_by = b[c-1]
            a = a[:r-1] + replace_by + a[r:]
            res.append(f'replace {replaced} by {replace_by} in a, \na is {a:>{string_len}}, \nb is {b:>{string_len}}')
            r-=1
            c-=1
        else:
            r-=1
            c-=1
    return res

def fprint(dp):
    for i in range(len(dp)):
        print(dp[i])
    print

def ed(a, b):
    la = len(a)
    lb = len(b)

    dp = [[0]*(lb+1) for _ in range(la+1)]
    for i in range(lb+1):
        dp[0][i] = i
    for i in range(la+1):
        dp[i][0] = i

    for i in range(1, la+1):
        for j in range(1, lb+1):
            dp[i][j] = min( dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + (1 if a[i-1]!=b[j-1] else 0) )

    fprint(dp)
    fprint(solution(dp, a, b))
    return dp[la][lb]

#print(ed('intention', 'execution'))
#print(ed('horse', 'ros'))
#print(ed('sunday', 'saturday'))
print(ed('AGGCTATCACCTGACCTCCAGGCCGATGCCC', 'TAGCTATCACGACCGCGGTCGATTTGCCCGAC'))