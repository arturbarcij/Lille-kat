s = input()
char_count = {}

result = ''.join(char for i, char in enumerate(s) if i == 0 or char != s[i - 1])
print(result)