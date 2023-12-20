def sort(m, n):
    if m < n:
        print(str(m) + " " + str(n))
    else:
        print(str(n) + " " + str(m))

line = input()
a, b = line.split()
a = int(a)
b = int(b)

sort(a,b)