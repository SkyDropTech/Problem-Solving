t=int(input())
res=""
for _ in range(t):
    n=int(input())
    x=max(15,((n+1)//2)*5)
    res+=str(x)+"\n"
print(res)