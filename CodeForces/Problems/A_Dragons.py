s,n=map(int,input().split())
t=[]
for _ in range(n):
    x,y=map(int,input().split())
    t.append((x,y))
t.sort()
for x,y in t:
    if s>x:
        s=s+y 
    else:
        print("NO")
        break 
else:
    print("YES")