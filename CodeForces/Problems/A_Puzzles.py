n,m=map(int,input().split())
f=list(map(int,input().split()))
f.sort()
min_val=float('inf')
i=0
while n+i<=m:
    maxi=f[i+n-1]
    mini=f[i]
    tot=maxi-mini
    min_val=min(tot,min_val)
    i+=1 
print(min_val)