n,m = map(int,input().split())
l= []

for i in range(n):
    l.append(input())

a = True

for i in range(n):
    for q in range(1,m):
        if l[i][q] != l[i][0]:
            a = False

    if i > 0:
        if l[i][0] == l[i-1][0]:
            a = False

if a == True:
    print("YES")
else:
    print("NO")

