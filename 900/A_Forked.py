import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    xk, yk = map(int, sys.stdin.readline().split())
    xq, yq = map(int, sys.stdin.readline().split())

    moves = {(a,b),(a,-b),(-a,b),(-a,-b),(b,a),(b,-a),(-b,a),(-b,-a)}

    king_pos = set()
    queen_pos = set()

    for dx, dy in moves:
        king_pos.add((xk + dx, yk + dy))
        queen_pos.add((xq + dx, yq + dy))

    print(len(king_pos & queen_pos))