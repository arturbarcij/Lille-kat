n = int(input())
height = 0
currBlocks = 0
sideLen = 1

while n >= currBlocks + sideLen ** 2:
    height += 1
    currBlocks += sideLen ** 2
    sideLen += 2

print(height)