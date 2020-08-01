tc = int(input()) # number of test cases
for i in range(tc):
    num = int(input())
    lst = list(map(int, input().split()))
    print(min(lst)+max(lst))
