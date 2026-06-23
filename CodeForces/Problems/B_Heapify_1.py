t=int(input())
res=""
for _ in range(t):
    n=int(input())
    X=True
    a=list(map(int,input().split()))
    lst=[]
    i=1
    for i in range(n):
        pos=i+1 
        val=a[i]
        while pos%2==0:
            pos//=2 
        while val%2==0:
            val//=2 
        if pos!=val:
            X=False 
            break
    if X:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)