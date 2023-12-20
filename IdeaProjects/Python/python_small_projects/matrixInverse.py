for n in range(5):
    row1 = input().split()
    row2 = input().split()
    a,b = map(int, row1)
    c,d = map(int, row2)
    print("Case {}:".format(n + 1))
    print(str(d) + " " + str(-b))
    print(str(-c) + " " + str(a))
    input()
