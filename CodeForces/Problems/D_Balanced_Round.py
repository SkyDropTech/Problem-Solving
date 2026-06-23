t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    maxlen=1
    count=1
    for i in range(1,n):
        if abs(a[i]-a[i-1])<=k: 
            count+=1 
        else:
            count=1
        maxlen=max(maxlen,count)
    res+=str(n-maxlen)+"\n"
print(res)
