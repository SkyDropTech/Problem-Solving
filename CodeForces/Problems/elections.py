t=int(input())
res=""
for _ in range(t):
    a,b,c=map(int,input().split())
    if a==b==c==0:
        res+="1 1 1\n" 
    
    else:
        if a==max(a,b,c) and [a,b,c].count(max(a,b,c))==1:
           m=0
        else:
           m=max(a,b,c)-a+1 
        if b==max(a,b,c) and [a,b,c].count(max(a,b,c))==1:
           n=0
        else:
           n=max(a,b,c)-b+1 
        if c==max(a,b,c) and [a,b,c].count(max(a,b,c))==1:
           o=0
        else:
           o=max(a,b,c)-c+1
        res+=f"{m} {n} {o}\n"
print(res)