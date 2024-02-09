n = int(input())
lst = [int(x) for x in input().split()]

A = [0]*n
A[0] = 1

for i in range(len(lst)):
    A[lst[i] + 1] = i + 2
print(*A)