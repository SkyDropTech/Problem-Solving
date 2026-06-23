t=int(input())
res=""
for _ in range(t):
    a,b=map(int,input().split())
    x=(a+b)//3
    y=min(a,b)
    res+=str(min(x,y))+"\n"
print(res) 