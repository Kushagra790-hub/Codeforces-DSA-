n = int(input())
a = list(map(int, input().split()))

a = sorted(set(a))

if len(a) < 2:
    print("NO")
else:
    print(a[1])