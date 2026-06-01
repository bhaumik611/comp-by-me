tc = int(input())
for _ in range(tc):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k == 2:
        print(0 if any(x % 2 == 0 for x in a) else 1)

    elif k == 3:
        print(min((3 - x % 3) % 3 for x in a))

    elif k == 5:
        print(min((5 - x % 5) % 5 for x in a))

    else: 
        total_twos = 0
        for x in a:
            if x % 2 == 0:
                total_twos += 1
            if x % 4 == 0:
                total_twos += 1

        if total_twos >= 2:
            print(0)
        else:
            cost4 = min((4 - x % 4) % 4 for x in a)

            costs = sorted((2 - x % 2) % 2 for x in a)
            cost2 = costs[0] + costs[1]

            print(min(cost4, cost2))