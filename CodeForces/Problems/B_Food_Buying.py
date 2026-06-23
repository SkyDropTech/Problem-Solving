t=int(input())
res=""
for _ in range(t):
    s=int(input())
    m=s
    suum=0
    while s>=10:
        r=s%10 
        d=s//10 
        s=d+r 
        suum+=d 
    suum+=m
    res+=str(suum)+"\n"
print(res)

    