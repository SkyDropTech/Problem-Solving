t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=abs(a[0])
    ct=0
    for i in range(1,n):
        if abs(a[i])<x:
            ct+=1 
    if ct <=n//2:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)