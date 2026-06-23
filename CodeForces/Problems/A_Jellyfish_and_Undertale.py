t=int(input())
res=""
for _ in range(t):
    a,b,n=map(int,input().split())
    x=list(map(int,input().split()))
    ct=0
    for i in range(n): 
        ct+=min(x[i],a-1)
    res+=str(b+ct)+"\n"
print(res)