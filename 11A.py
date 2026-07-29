n,k = map(int,input().split())
l = list(map(int,input().split()))
u,g = 0,0
for i in range(1,n):
    if l[i] <= l[i-1]:
        u = (l[i - 1] - l[i]) // k + 1
        l[i] += k*u
        g += u

print(g)