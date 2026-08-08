n = int(input())

ans = 0

for i in range(2, n + 1):
    cnt = 0
    x = i

    d = 2
    while d * d <= x:
        if x % d == 0:
            cnt += 1
            while x % d == 0:
                x //= d
        d += 1

    if x > 1:
        cnt += 1

    if cnt == 2:
        ans += 1

print(ans)