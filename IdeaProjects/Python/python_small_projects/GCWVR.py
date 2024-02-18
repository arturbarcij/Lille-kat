G, T, N = map(int, input().split())

#for i in range(N):
def maxWeight(G, T, N):
    weightList = [int(N) for N in input().split()]
    weight = 0.9 * (G - T) - (sum(weightList))
    return weight

print(int(maxWeight(G, T, N)))