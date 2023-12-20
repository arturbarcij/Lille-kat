cases = int(input())


for case in range(1, cases + 1):
    noGuests = int(input())
    guests = list(map(int, input().split()))
    
    aloneGuest = 0
    for guest in guests:
        aloneGuest ^= guest
    
    
    print(f"Case #{case}: {aloneGuest}")
