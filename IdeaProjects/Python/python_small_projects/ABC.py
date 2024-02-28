numList = list(map(int, input().split()))
order = input().strip()
orderMap = {char: i for i, char in enumerate(order)}
sortNum = 0
if len(numList) != 0 and len(numList) == len(orderMap):
    sortNum = [(orderMap[char], num) for num, char in zip(numList, numList)]

sorted_numbers = sorted(sortNum, key=lambda x: x[0])

print(sorted_numbers)
