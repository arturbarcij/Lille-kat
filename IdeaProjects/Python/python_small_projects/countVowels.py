def countVowels(s):
    count = 0
    for character in range(len(s)):
            if (
                ((s[character] == 'a') or (s[character] == 'A'))
                or ((s[character] == 'e') or (s[character] == 'E'))
                or ((s[character] == 'i') or (s[character] == 'I'))
                or ((s[character] == 'o') or (s[character] == 'O'))
                or ((s[character] == 'u') or (s[character] == 'U'))
            ):
                count += 1
    return count


ss = input()
print(countVowels(ss))