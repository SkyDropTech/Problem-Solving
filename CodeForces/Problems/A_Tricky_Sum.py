t=int(input())
res=""
for _ in range(t):
    n=int(input())
    sum1=(n*(n+1))//2
    p=1
    suum=0
    while p<=n:
        suum+=p 
        p=p*2 
    sum2=2*(suum)
    res+=str(sum1-sum2)+"\n"
print(res)