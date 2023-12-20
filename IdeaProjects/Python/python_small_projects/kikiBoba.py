line = input()

if len(line) < 2:
    if 'b' in line:
        print("boba")
    elif 'k' in line:
        print("kiki")
    else:
        print("none")
else:
    if line.count('b') > line.count('k'):
        print("boba")
    elif line.count('b') < line.count('k'):
        print("kiki")
    elif (line.count('b') == line.count('k')) and line.count('b') > 0:
        print("boki")
    else:
        print("none")