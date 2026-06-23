t = int(input())
for _ in range(t):
    n = int(input())
    res=[]
    res.append(2)
    i=n
    while i>2:
        res.append(i)
        i-=1
    res.append(1)     

    for x in res:
        print(x, end=" ")
    print()