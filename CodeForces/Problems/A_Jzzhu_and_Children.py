n,m=map(int,input().split())
a=list(map(int,input().split()))
d1={}
d2={}
count=0
for i in range(n):
    if a[i]>m:
        d1[a[i]]=i 
        count+=1 
if count==n:
    print(n)
else:
    if d1:
        mx=0
        pos=-1
        
        for key in d1:
            q=key//m
            if q>mx:
                mx=q
                pos=d1[key]
        
        if mx>1:
            print(pos+1)
