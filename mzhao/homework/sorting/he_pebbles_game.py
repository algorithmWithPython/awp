import math
tc = int(input())

# basically we need to calculate an area

#   min0  min_1
#          /------------------------|
#         /                         |
#        /                          |
#       /                           |
#      /                            |
#      |                            |
#      |                            |
#      |                            |
#           .... 
#      |                            |
#      |                            |
#      |                           /
#      |                          /
#      |                         /
#      |                        /
#      |                       /
#      -----------------------/
#                          max_1  max_0

for _ in range(tc):
    p_num, cost = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    min_0 = p[0]
    min_1 = p[1]
    max_0 = p[-1]
    max_1 = p[-2]

    t = (max_0-min_1) + (max_1-min_0)
    t += math.ceil(math.sqrt(2)*((min_1-min_0)+(max_0-max_1)))
    t += max_1-min_0
    t += max_0-min_1
    print(int(t*cost))