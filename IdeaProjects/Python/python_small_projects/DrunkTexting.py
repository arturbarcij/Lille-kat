drunkText = input()
inoLine = input()

r = ''.join(char for i, char in enumerate(drunkText) if i == 0 or char != drunkText[i - 1])
r2 = ''.join(char for i, char in enumerate(inoLine) if i == 0 or char != inoLine[i - 1])

c = []
for x in range(max(len(r2), len(r))):
    c.append(r[x] if x < len(r) else '')
    c.append(r2[x] if x < len(r2) else '')

result = ''.join(c)
print(result)

# Sorting and printing characters from inoLine
sorted_chars = ''.join(''.join(x) for x in sorted(zip(r2, r)))
print(sorted_chars)
