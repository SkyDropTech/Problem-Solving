t=int(input())
res=""
for _ in range(t):
    n,m=map(int,input().split())
    if n>=m and (n-m)%2==0 :
        res+=str("YES")+"\n"
    else:
        res+=str("NO")+"\n"
print(res)