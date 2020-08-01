import random
def shell_sort(b):
    a = list(b)
    l = len(a)
    d = 1
    while d < l//3:
        d = 3*d+1 # 1, 4, 13, 40, 121, 364, 1093, ...
    while d>0:
        for i in range(d, l):
            j = i
            v = a[i]
            while j>=d and a[j-d]>v:
                a[j]=a[j-d]
                j-=d
            a[j] = v
        d = d//3
    return a

if __name__ == "__main__":
    l=[]
    for i in range(20):
        l.append(random.randint(-100, 100))
    print(l)
    print(shell_sort(l))
