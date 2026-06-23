n,m=map(int,input().split())
if m%n!=0:
    print(-1)
else:
    ct=0
    a=m//n
    while a%2==0:
        a//=2
        ct+=1 
             
    while a%3==0:
        a//=3 
        ct+=1 
    if a!=1:
        print(-1)
    else:
        print(ct)
