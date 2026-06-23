def numberofpostion(n,a,b):
    ct=0
    for i in range(1,n+1):
        if i-1>=a and n-i<=b:
            ct+=1 
    return ct
n,a,b=map(int,input().split())
print(numberofpostion(n,a,b))