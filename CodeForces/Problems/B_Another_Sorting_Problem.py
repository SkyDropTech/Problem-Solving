t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    maxi=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            x=a[i]-a[i+1]
            maxi=max(x,maxi)
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i+1]=a[i+1]+maxi 
    if a==sorted(a):
        res+="YES\n"
    else:
        res+="NO\n"
print(res)
    
