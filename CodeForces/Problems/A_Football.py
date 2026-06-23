n=int(input())
lst=[]
lsst=[]
for _ in range(n):
    s=input().upper()
    lst.append(s) 
r=max(lst,key=lst.count)
print(r)