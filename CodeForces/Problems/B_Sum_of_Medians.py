t = int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=(n+1)//2
    skip=n-m
    pos=n*k-(skip+1)
    ans=0
    for _ in range(k):
        ans+=a[pos]
        pos-=(skip+1)
    res+=str(ans)+"\n"  
print(res)