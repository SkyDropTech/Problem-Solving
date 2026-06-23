t=int(input())
res=""
for _ in range(t):
    n,a,b=map(int,input().split())
    s=input()
    if b>=0:
        ans=n*(a+b) 
        res+=str(ans)+"\n"
    else:
        
print(res)