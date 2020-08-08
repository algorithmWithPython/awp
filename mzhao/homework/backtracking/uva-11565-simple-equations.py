tc = int(input())
for _ in range(tc):
    A, B, C = map(int, input().split())
    done = False
    for i in range(-21, 22, 1):
        if i*i >= C:
            continue
        if done:
            break
        for j in range(-100, 100):
            if i == j or i*i + j*j > C:
                continue
            if done:
                break
            for k in range(-100, 100):
                if k!=i and k!=j and i+j+k == A and i*j*k == B and i*i + j*j + k*k == C:
                    print(i,j,k)
                    done = True
                    break
    if not done:
        print("No solution.")
