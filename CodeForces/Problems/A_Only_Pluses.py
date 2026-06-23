t=int(input())
res=""
for _ in range(t):
    a,b,c=map(int,input().split())
    n=5 
    for i in range(n):
        if a<=b and a<=c :
            a+=1 
        elif b<=c and b<=a :
            b+=1 
        else:
            c+=1 
    res+=str(a*b*c)+"\n"
print(res)