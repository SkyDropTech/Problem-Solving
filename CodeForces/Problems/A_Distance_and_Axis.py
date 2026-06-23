t=int(input())
res="" 
for _ in range(t):
    n,k=map(int,input().split())
    if n>=k:
        if (n+k)%2==0:
            res+=f"{0}\n"
        else:
            res+=f"{1}\n"
    else:
        res+=f"{k-n}\n"
print(res)