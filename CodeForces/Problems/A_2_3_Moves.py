t=int(input())
res=""
for _ in range(t):
    n=int(input())
    if n<5:
        if n==1:
            res+=str(2)+"\n"
        elif n==2:
            res+=str(1)+"\n"
        elif n==3:
            res+=str(1)+"\n"
        else:
            res+=str(2)+"\n"
    else:
        x=n//3
        if n%3==0:
            res+=str(x)+"\n"
        else:
            res+=str(x+1)+"\n"
print(res)