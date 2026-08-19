t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    x = max(a, b, c)
    y = min(a, b, c)
    z = a + b + c - x - y

    ans = x - y

    # Replace the largest with the sum of the other two
    new_max = max(y, z, y + z)
    new_min = min(y, z, y + z)
    ans = min(ans, new_max - new_min)

    # Replace the middle with the sum of the other two
    new_max = max(y, x, y + x)
    new_min = min(y, x, y + x)
    ans = min(ans, new_max - new_min)

    # Replace the smallest with the sum of the other two
    new_max = max(z, x, z + x)
    new_min = min(z, x, z + x)
    ans = min(ans, new_max - new_min)

    print(ans)