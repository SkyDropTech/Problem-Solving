t=int(input())
res=""
for _ in range(t):
    a,b,c=map(int,input().split())
    if a<c:
        x=1 
    else:
        x=-1 
    if a*b>c:
        y=b 
    else:
        y=-1 
    res+=f"{x} {y}\n"
print(res)