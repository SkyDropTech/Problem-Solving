t=int(input())
res=""
for _ in range(t):
    x,n=map(int,input().split())
    if x%2==0:
        if n%4==0:
            res+=str(x)+"\n"
        elif n%4==1:
            res+=str(x-n)+"\n"
        elif n%4==2:
            res+=str(x+1)+"\n"
        else:
            res+=str(x+n+1)+"\n"
    else:
        if n%4==0:
            res+=str(x)+"\n"
        elif n%4==1:
            res+=str(x+n)+"\n"
        elif n%4==2:
            res+=str(x-1)+"\n"
        else:
            res+=str(x-n-1)+"\n"
print(res)

