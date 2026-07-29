n, k = map(int,input().split())
l= list(map(int,input().split()))
p = 0
u = l[k-1]
for i in l:
    if i >= u and i  > 0: 
        p += 1 

print(p)

