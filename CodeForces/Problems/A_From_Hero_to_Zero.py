t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split())
    ct=0
    while n!=0:
        if n%k!=0:
            r=n%k
            ct+=r
            n=n-r
        else:
            n=n//k 
            ct+=1 
    res+=str(ct)+"\n"
print(res)