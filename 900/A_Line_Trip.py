t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    max_dist = a[0]
    for i in range(1, n):
        max_dist = max(max_dist, a[i] - a[i-1])
    max_dist = max(max_dist, 2 * (x - a[-1]))
    print(max_dist)