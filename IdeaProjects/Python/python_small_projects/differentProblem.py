try:
    while True:
        a,b = [int(x) for x in input().split()]
        print(abs(a - b))
except EOFError:
    pass