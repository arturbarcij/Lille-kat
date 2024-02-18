n = int(input())
for i in range(n):
    b, p = [float(x) for x in input().split()]
    BPM = (60 * b) / p
    minABPM = 60 / (p / (b - 1))
    maxABPM = 60 / (p / (b + 1))
    print("{:.4f} {:.4f} {:.4f}".format(minABPM, BPM, maxABPM))