def multipliaction_Table(n,x):
    ct=0
    for i in range(1,n+1):
        if x%i==0:
            j=x//i 
            if j<=n:
                ct+=1 
    return ct 
n,x=map(int,input().split())
print(multipliaction_Table(n,x))
