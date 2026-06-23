t=int(input())
res=""
for _ in range(t):
    n=int(input())
    x=n%3 
    if x==0:
        res+=str(0)+"\n"
    else:
        y=3-x 
        res+=str(y)+"\n"
print(res)