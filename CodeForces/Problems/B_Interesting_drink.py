n=int(input())
x=list(map(int,input().split()))
x.sort()
q=int(input()) 
arr=[]
for i in range(q):
    m=int(input())
    arr.append(m)
for target in arr:
    l=0 
    r=n-1 
    while l<r:
        mid=(l+r)//2 
        if x[mid]==target:
            break
        elif x[mid]>target:
            r=mid-1 
        else:
            l=mid+1 
 
            
            
    
    