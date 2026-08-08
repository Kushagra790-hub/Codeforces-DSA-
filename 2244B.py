t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix = 0
    possible = True

    for i in range(n):
        prefix += a[i]

        need = (i + 1) * (i + 2) // 2

        if prefix < need:
            possible = False
            break

    print("YES" if possible else "NO")