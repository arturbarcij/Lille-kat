from datetime import datetime
try:
    s = input()
    format = datetime.strptime(s, "%b %d")
    if (format.month == 10 and format.day == 31) or (format.month == 12 and format.day == 25):
        print("yup")
    else:
        print("nope")
except ValueError:
    print("nope")