a = int(input())

for _ in range(a):
    n, s, x = map(int, input().split())
    a = list(map(int, input().split()))

    total = sum(a)
    
    if s>=total and (s-total)%x==0:
        print("YES")
    else:
        print("NO")
