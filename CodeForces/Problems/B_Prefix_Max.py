t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    x=max(a)
    res+=str(x*n)+"\n"
print(res)
