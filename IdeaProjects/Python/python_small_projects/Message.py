rows, columns = map(int, input().split())
grid = [input() for i in range(rows)]

message = ''.join(char for row in grid for char in row if char.isalpha())

'''
letters_only = ''
for row in grid:
    for char in row:
        if char.isalpha():
            message += char
'''
print(message)