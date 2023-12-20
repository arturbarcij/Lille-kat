n = int(input())
factorials = []


def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result = (result * i) % 10
        return result


for i in range(n):
    local = factorials
    f = int(input())
    local.append((factorial(f)))


for lastDigit in factorials:
    print(lastDigit)