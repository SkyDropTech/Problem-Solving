t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    if n%2==0:
        res+="YES\n"
    else:
        if k%2==0:
            res+="NO\n"
        else:
            res+="YES\n"
print(res)