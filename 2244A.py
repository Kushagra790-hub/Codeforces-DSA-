t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    longest = 0
    current = 0

    for ch in s:
        if ch == '#':
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    print((longest + 1) // 2)