m = input('')
n = input('')
list1 = []
value = ""
for x in m:
    if x != " ":
        value = value + x
    else:
        list1.append(value)
        value = ""
list1.append(value)
count = 0
for x in list1:
    if x != " " and int(n) >= int(x):
        count = count + 1
if count == 0:
    print("F")
elif count == 1:
    print("E")
elif count == 2:
    print("D")
elif count == 3:
    print("C")
elif count == 4:
    print("B")
else:
    print("A")
