t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    groups = 1

    for i in range(1, n):
        if s[i] != s[i - 1]:
            groups += 1

    ans = groups

    for i in range(1, n - 1):
        cur = 0

        if s[i] != s[i - 1]:
            cur += 1

        if s[i] != s[i + 1]:
            cur += 1

        if s[i - 1] != s[i + 1]:
            cur -= 1

        ans = min(ans, groups - cur)

    print(ans)