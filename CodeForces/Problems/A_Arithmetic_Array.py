t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    suum=sum(a)
    if n<suum:
        x=suum-n 
    elif n==suum:
        x=0 
    else:
        x=1
    res+=str(x)+"\n"
print(res)