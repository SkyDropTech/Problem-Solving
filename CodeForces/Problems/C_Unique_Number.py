t=int(input())
res=""
for _ in range(t):
    n=int(input())

    if n>45:
        res+="-1\n"
        continue
    
    digits=[]
    d=9 
    while n>0:
        if n>=d:
            digits.append(d)
            n=n-d 
        d-=1 

    digits.reverse()
    res+="".join(map(str,digits))+"\n"
print(res)

