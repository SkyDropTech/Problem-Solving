t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    b=input()

    if a.count("1")!=b.count("1"):
        print("NO")
        continue
    x=0
    y=0

    for i in range(0,n,2):
        if a[i]=="1":
            x+=1
        if b[i]=="1":
            y+=13

    if x==y:
        print("YES")
    else:
        print("NO")