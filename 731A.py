s = input()

ans = 0
current = ord('a')

for ch in s:
    next_char = ord(ch)
    diff = abs(current - next_char)
    ans += min(diff, 26 - diff)
    current = next_char

print(ans)