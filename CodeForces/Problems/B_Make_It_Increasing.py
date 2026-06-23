t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    
    ct=0
    ok=True
    for i in range(n-2,-1 ,-1 ):
    
        while a[i]>=a[i+1] and a[i]>0:
            a[i]=a[i]//2 
            ct+=1 
        if a[i]>=a[i+1]:
            ok=False 
            break
    if ok:
        res+=str(ct)+"\n"
    else:
        res+="-1\n"
print(res)
