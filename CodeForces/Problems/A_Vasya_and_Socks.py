n,m=map(int,input().split())
i=1
count=0
while m*i<=n+count: 
    count+=1
    i+=1 
print(n+count)