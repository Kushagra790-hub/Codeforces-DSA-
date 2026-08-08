s = input().strip()

i = 0
ans = ""

while i < len(s):
    if s[i] == '.':
        ans += '0'
        i += 1
    elif s[i:i+2] == '-.':
        ans += '1'
        i += 2
    else:  # "--"
        ans += '2'
        i += 2

print(ans)