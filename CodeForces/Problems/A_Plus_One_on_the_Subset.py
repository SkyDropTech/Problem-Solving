t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    maxi=max(a)
    mini=min(a)
    res+=str(maxi-mini)+"\n"
print(res)
