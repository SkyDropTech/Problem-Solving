t=int(input())
res="" 
for _ in range(t):
    n=int(input())
    x=list(map(int,input().split()))
    a=[0]*n 
    a[0]=1000
    for i in range(1,n):
        a[i]=a[i-1]+x[i-1]
    print(*a)
print()