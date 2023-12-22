#Input
s = input()
# Split the string based on "()"
parts = s.split("()")

# Extract the prefix and suffix
prefix = parts[0]
suffix = parts[1] if len(parts) > 1 else ""

if (s.startswith('|') and s.endswith('|')):
    if prefix == suffix:
        print("correct")
    else:
        print("fix")
else:
    print("fix")
