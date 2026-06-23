n=int(input())
num=list(map(int,input().split()))
lst1=[] 
lst2=[]
for i in range(n):
    if num[i]%2==0:
        lst1.append(i+1) 
    else:
        lst2.append(i+1) 
if len(lst1)==1:
    print(*lst1) 
if len(lst2)==1:
    print(*lst2)