# n k x 
def is_valid(n, k, x):
    min_sum = (k * (k + 1)) // 2
    max_sum = (k * (2 * n - k + 1)) // 2
    return min_sum <= x <= max_sum

t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    if is_valid(n, k, x):
        print("YES")
    else:
        print("NO")


