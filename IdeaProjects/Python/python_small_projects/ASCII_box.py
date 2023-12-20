n = int(input())

hyphen = '-'
line = '|'
tb = 0
lf = 0

if n > 0:
    for size in range(n + 1):
        tb = hyphen * size

    print("+" + str(tb) + "+")

    for i in range(n):
        print(str(line) + ((" ")*n) + str(line))
        
    print("+" + str(tb) + "+")
else:
    print("++")
    print("++")