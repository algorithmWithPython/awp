first=True
while True:
    n = int(input())
    if n == 0:
        break

    if not first:
        print()
    else:
        first = False    
    
    def get_digits(i):
        res = set()
        while i>0:
            res.add(i%10)
            i //=10
        return res

    good = False
    for i in range(1234, 98765//n+1):
        down = get_digits(i)
        if i<10000:
            down.add(0)
        if len(down) == 5:
            up = get_digits(i*n)
            if len(up|down) == 10 and len(up&down)==0:
                good = True
                print(f'{i*n} / {i:0>5} = {n}')

    if not good:
        print(f'There are no solutions for {n}.')
    