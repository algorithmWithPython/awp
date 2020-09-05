mem={}
def ways(pies, persons, minPiePerPerson):
    if (pies, persons, minPiePerPerson) in mem:
        return mem[(pies, persons, minPiePerPerson)]
    if persons == 1:
        return 1
    if pies == persons:
        return 1
    if pies < persons:
        return 0
    maxPiePerPerson = pies // persons
    count = 0
    for i in range(minPiePerPerson, maxPiePerPerson+1):
        count += ways(pies-i, persons-1, i)
    mem[(pies, persons, minPiePerPerson)] = count
    return count

npie=int(input())
nperson = int(input())

print( ways(npie, nperson, 1))