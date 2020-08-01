num = int(input())
lst = list(map(int, input().split())) # powers of zombies and vampires

z = [] # hold powers of zombies
z_sum = 0 # total power of zombies
v = [] # hold powers of vampires
v_sum = 0 # total power of vampires
for i in lst:
    if i%2==0:
        z.append(i)
        z_sum += i
    else:
        v.append(i)
        v_sum -= i

# print out result
for i in sorted(z):
    print(i, end=" ")
print(z_sum, end=" ")

for i in sorted(v):
    print(i, end=" ")
print(v_sum)
