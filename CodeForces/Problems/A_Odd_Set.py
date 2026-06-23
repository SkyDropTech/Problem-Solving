t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    lst1=[]
    lst2=[]
    for i in range(2*n):
        if a[i]%2==0:
            lst1.append(a[i])
        else:
            lst2.append(a[i])
    if len(lst1)==len(lst2):
        res+="YES\n"
    else:
        res+="NO\n"
print(res)