t=int(input())
res=""
for _ in range(t):
    n=int(input())
    lst=[]
    a=list(map(int,input().split()))
    for x in a:
        if x not in lst:
            lst.append(x)
    res+=" ".join(map(str, lst))+"\n"
print(res)