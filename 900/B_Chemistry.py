t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    freq = [0]*26

    for c in s:
        freq[ord(c)-97] += 1

    odd = sum(f % 2 for f in freq)

    if odd <= k + 1:
        print("YES")
    else:
        print("NO")