t=int(input())
res=""
for _ in range(t):
    n=int(input())
    
    if n<4 or n%2!=0:
        res+="-1\n"
    elif n%6==0:
        res+=f"{n//6} {n//4}\n"
    
    elif n%4==0:
        if n%6==2 or n%6==4:
            res+=f"{(n//6)+1} {n//4}\n"
    else:
        if n%6==2 or n%6==4:
            res+=f"{(n//6)+1} {n//4}\n"
        else:
            res+="-1\n"

print(res)