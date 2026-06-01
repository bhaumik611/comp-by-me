import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s = input().strip()
    
    c0 = s.count('0')
    c1 = s.count('1')
    
    length = 0
    
    for ch in s:
        if ch == '0':
            if c1 > 0:
                c1 -= 1
                length += 1
            else:
                break
        else:  # ch == '1'
            if c0 > 0:
                c0 -= 1
                length += 1
            else:
                break
    
    # deletions = total length - kept length
    print(len(s) - length)