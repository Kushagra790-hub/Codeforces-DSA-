t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = input().strip()
    s = input().strip()

    ans = -1

    for i in range(6):
        if s in x:
            ans = i
            break
        x += x

    print(ans)