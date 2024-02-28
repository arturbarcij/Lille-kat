N = int(input())
ta,da = list(map(int, input().split()))
tb,db = list(map(int, input().split()))

secondsAli = 0
secondsBob = 0
for c in range(N):
    secondsAli += ta + da*c
    secondsBob += tb + db*c

if secondsAli < secondsBob:
    print("Alice")
elif secondsAli == secondsBob:
    print("=")
elif secondsBob < secondsAli:
    print("Bob")