def fib_bt(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_bt(n-1) + fib_bt(n-2)

# O(2^n), O(n!) => O(n), O(n^2), O(n^3)
def fib_mem(n): #top-down # n*O(1) = O(n)
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib = [-1]*(n+1)
    fib[0], fib[1] = 0, 1
    def _fib(n):
        if fib[n] == -1:
            fib[n] = _fib(n-1) + _fib(n-2) # O(1)
        return fib[n]

    return _fib(n)

def fib_iterative(n): #bottom-up # O(n) O(n)
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[-2]+fib[-1])
    return fib[n]

def fib_iterative_space_efficient(n): #bottom-up O(1)
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev_1 = 1
    prev_2 = 0
    for i in range(2, n+1):
        fib = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = fib
    return fib

i=34
print(fib_mem(i))
print(fib_iterative(i))
print(fib_iterative_space_efficient(i))
print(fib_bt(i))
print()
