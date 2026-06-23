t=int(input())
res=""
for _ in range(t):
    x,y,k=map(int,input().split())
    m1=k*(y+1)
    m2=m1-1//x-1
    m=(k*(y+1))-1//(x-1)
    res+=str(k+m2)+"\n"
print(res)