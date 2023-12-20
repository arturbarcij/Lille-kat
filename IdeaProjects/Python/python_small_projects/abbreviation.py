s = input()
uppercaseLetters = ''
for word in s.split('-'):
    uppercaseLetters += word[0]

print(uppercaseLetters)     