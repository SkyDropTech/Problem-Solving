n=int(input())
a=list(map(int,input().split()))
swap=0
for i in range(n-1):
    for j in range(n-i-1):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j] 
            swap+=1 
print(swap)