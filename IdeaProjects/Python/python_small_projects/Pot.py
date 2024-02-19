n = int(input())
sumList = 0

for _ in range(n):
    addend = int(input())
    lastDigit = addend % 10
    originalNum = addend // 10
    sumList += originalNum ** lastDigit
    # int(str(addend)[-1])

print(sumList)
