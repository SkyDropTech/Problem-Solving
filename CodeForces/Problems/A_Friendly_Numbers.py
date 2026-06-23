t=int(input())
res=""
for _ in range(t):
    x=int(input())
    count=0
    for y in range(x,x+101):
        if y-sum(map(int,str(y)))==x:
            count+=1
    res+=str(count)+"\n"
print(res)