t=int(input())
res=""
for _ in range(t):
    n,s,t=map(int,input().split())
    
    res+=str(max(n-s,n-t)+1)+"\n"
print(res)