import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k, m = map(int, input().split())

    if m == 1:
        if k == 1:
            print("YES")
            print(*([1] * n))
        else:
            print("NO")
        continue

    if k > m:
        print("NO")
        continue

    print("YES")

    a = [1] * n
    a[k - 1] = m - k + 1

    print(*a)