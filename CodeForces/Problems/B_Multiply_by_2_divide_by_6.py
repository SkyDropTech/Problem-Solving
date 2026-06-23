t=int(input())
res=""
for _ in range(t):
    n=int(input())
    ct=0
    if n==1:
        res+="0\n"
    else:
        while n!=1:
            if n%3!=0:
                ct=-1
                break 
            if n%6==0:
                n=n//6 
                ct+=1 
            else:
                n=n*2 
                ct+=1
        if n==1:
            res+=str(ct)+"\n"
        else:
            res+=str(ct)+"\n"
print(res)