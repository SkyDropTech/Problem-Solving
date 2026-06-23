t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    cur=a[0]
    ans=0
    
    for i in range(n):
        cur=min(cur,a[i])
        ans+=cur
        
    best=ans
    
    cur=a[0]
    s=0
    
    for j in range(1,n):
        cur=min(cur,a[j-1])
        s+=cur
        best=min(best,s)
        
    print(best)