s = input()
l = len(s)

whiteSpace = sum(1 for char in s if char == '_' or char.isspace())
lowerCase = sum(1 for char in s if char.islower())
upperCase = sum(1 for char in s if char.isupper())
symbols = l - (whiteSpace + lowerCase + upperCase)


rWS = whiteSpace / l
rLC = lowerCase / l
rUC = upperCase / l
rS = symbols / l

print(f"{rWS:.10f}")
print(f"{rLC:.10f}")
print(f"{rUC:.10f}")
print(f"{rS:.10f}")