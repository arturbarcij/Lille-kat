lst = []
sumList = []
for i in range(5):
    g1, g2, g3, g4 = [int(x) for x in input().split()]
    lst = [g1, g2, g3, g4]
    Sum = sum(lst)
    sumList.append(Sum)

sortedArr = sorted(sumList)
#max(sumList)
print(str((sumList.index(max(sumList))) + 1) + " " + str(sortedArr[-1]))
