n,t=map(int,input().split())
low=10**(n-1)+1 
high=10**n 
for i in range(low,high):
    if i%t==0:
        print(i)
        break 
else:
    print(-1)
        
