t=int(input())
res=""
for _ in range(t):
    s=input()
    bal=0 
    t=False 
    for i in range(len(s)-1):
        if s[i]=="(":
            bal+=1 
        else:
            bal-=1 
        if bal==0:
            t=True 
            break 
    if t:
        res+="YES\n"
    else:
        res+="NO\n"
print(res)
