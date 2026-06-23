t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split())) 
    x=sorted(a)
    if n>1:
        for i in range(n-1):
            if x == a:
                count=n
            else:
                count=1     
    else:
        count=1 
    res+=str(count)+"\n"

print(res)