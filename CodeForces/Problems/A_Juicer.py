n,b,d=map(int,input().split())
a=list(map(int,input().split()))
suum=0
count=0
for i in range(n):
    if a[i]>b:
        continue 
    else:
        suum+=a[i]
        if suum>d:
            count+=1
            suum=0
print(count)