t=int(input())
res=""
for _ in range(t):
    lst=[]
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(n):
        if a[i]==1:
            lst.append(i)
            break 
    a=a[::-1]
    for j in range(n):
        if a[j]==1 :
            lst.append(n-j)
            break
    m=lst[1]-lst[0]
    if m<=x:
        res+=str("YES")+"\n"
    else:
        res+=str("NO")+"\n"
print(res)