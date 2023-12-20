line = input()
classrooms, numBottles = map(int, line.split())
sum = 0
for _ in range(classrooms):
    bottles = input()
    sum += bottles
    if sum <= numBottles:
        print("Jebb")
    else:
        print("Neibb")
