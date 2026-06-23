t=int(input())
res=""
for _ in range(t):
    a,b=map(int,input().split())
    suum=a+b 
    if suum%2==0:
        res+=str("Bob")+"\n"
    else:
        res+=str("Alice")+"\n"
print(res)