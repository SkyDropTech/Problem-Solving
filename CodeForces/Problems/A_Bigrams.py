t=int(input())
for _ in range(t):
    k=int(input())
    c=list(map(int,input().split()))
    ok=False 
    two=0
    for i in range(k):
        if c[i]>=3:
            ok=True
        if c[i]>=2:
            two+=1 
        
    if ok or two>=2 :
        print("YES")
    else:
        print("NO")

