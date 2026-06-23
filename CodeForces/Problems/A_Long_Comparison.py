t=int(input())
res=""
for _ in range(t):
    x1,p1=map(int,input().split())
    x2,p2=map(int,input().split())
    xt1=str(x1)+"0"*p1
    xt2=str(x2)+"0"*p2 
    if len(xt1)>len(xt2):
        res+=">\n"
    elif len(xt1)<len(xt2):
        res+="<\n"
    elif xt1>xt2:
        res+=">\n"
    elif xt1<xt2:
        res+="<\n"
    else:
        res+="=\n"
print(res)
    