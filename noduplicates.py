a = input()
b = set(a.split(" "))
if len(b) == len(a.split(" ")):
    print("yes")
else:
    print("no")