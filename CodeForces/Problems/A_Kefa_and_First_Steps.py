n=int(input())
a=list(map(int,input().split()))
max_val=1 
ct=1
for i in range(n-1):
    if a[i]<=a[i+1]:
        ct+=1 
        max_val=max(max_val,ct) 
    else:
        ct=1
    
print(max_val)
