'''
1

2 1

3 5 8

55 34 21 13

89 144 233 377 610

10946 6765 4181 2584 1597 987
'''

from ast import pattern

inp = int(input("Enter the number of rows: "))
fibo = [1, 1]
pattern = []
for i in range(inp):
    if i > 1:
        fibo.append(fibo[i-1] + fibo[i-2])
    row = []
    for j in range(i+1):
        row.append(fibo[j])
    pattern.append(row)

a = 1
new_pattern = []
for i in range(len(fibo)):
    if a == 1:
        new_pattern.append([fibo[i]])
        c = i
        a = -1
    elif a == -1:
        new_pattern.append([fibo[c:i]])
        c = i
        a = 1

for row in new_pattern:
    print(*row)