t=int(input())
res=""
for _ in range(t):
    lst=[]
    n=int(input())
    a=list(map(int,input().split()))
    t=True
    for i in range(n-1):
        a[i]-=1
        if a[i]<0:
            lst.append(0)
        else:
            a[i+1]+=1 
            lst.append(a[i])
        lst.append(a[i+1])
    for j in range(len(lst)-1):
        if lst[j]<lst[j+1]:
            t=False
            break 
    if t:
        res+="NO\n"
    else:
        res+="YES\n"
print(res)