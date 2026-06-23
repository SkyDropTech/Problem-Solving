t=int(input())
res=""
for _ in range(t):
    n,k,x=map(int, input().split())
    mn=k*(k+1)//2
    mx=k*(2*n-k+1)//2
    if mn<=x<=mx:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)