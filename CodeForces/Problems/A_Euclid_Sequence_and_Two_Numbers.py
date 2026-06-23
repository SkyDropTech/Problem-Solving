t=int(input())
res=""
for _ in range(t):
    n=int(input())
    b=list(map(int,input().split()))
    b.sort()
    a=b[::-1]

    found=True
    for i in range(n-2):
        if a[i]%a[i+1]!=a[i+2]: 
            found = False
            break
    if  found:
        print(a[0],a[1])
    else:
        print(-1)


