t=int(input())
res=""
for _ in range(t):
    n=int(input())
    i=0
    while True:
        x=str(n)
        ok = True
        
        for ch in x:
            if ch!="0" and n%int(ch)!=0:
                ok=False
                break
        if ok:
            res+=f"{n}\n"
            break 
        n+=1
print(res)
