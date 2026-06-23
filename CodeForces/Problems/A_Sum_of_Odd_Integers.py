t=int(input())
res=""
for _ in range(t):
    n,k=map(int,input().split()) 

    if n%2==0 and k%2!=0 :
        res+=str("NO")+"\n"
    else:
        res+=str("YES")+"\n"
print(res)