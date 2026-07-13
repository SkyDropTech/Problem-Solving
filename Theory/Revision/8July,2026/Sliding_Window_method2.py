n=int(input())
a=list(map(int,input().split()))
k=int(input())
suum=0
ans=0
for i in range(n-k+1):
    suum=sum(a[i:i+k] )
    ans=max(ans,suum) 
print(ans)