t=int(input())
res="" 
for _ in range(t):
    a,b,c=map(int,input().split())
    m=min(a,b,c) 
    if a%m!=0 or b%m!=0 or c%m!=0:
        res+="NO\n"
    else:
        q=a//m 
        w=b//m 
        e=c//m 
        suum=(q+w+e)-3 
        if suum<=3:
            res+="YES\n"
        else:
            res+="NO\n"
print(res)