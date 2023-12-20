n = int(input())
oddStrings = []


for i in range(n):
    local = oddStrings
    word = input()
    if (i-1) % 2 != 0:
        (local.append(word))


for oddStr in oddStrings:
    print(oddStr)