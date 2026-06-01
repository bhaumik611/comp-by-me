a = int(input())
for i in range(a):
    b = input()
    bl = b.split()
    if int(bl[0]) == int(bl[1]) and int(bl[1]) == int(bl[2]) and int(bl[2]) == int(bl[3]):
        print("YES")
    else:
        print("NO")