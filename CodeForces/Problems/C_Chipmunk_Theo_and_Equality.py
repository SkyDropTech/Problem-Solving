t=int(input())
res=""
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    maxi=0
    for i in range(n-1):
        if a[i]>a[i+1]:
            x=a[i]-a[i+1]
            maxi=max(x,maxi)
    for i in range(n-1):
        if a[i]>a[i+1]:
            a[i+1]=a[i+1]+maxi 
    if a==sorted(a):
        res+="YES\n"
    else:
        res+="NO\n"
print(res)
    


4 6 8 16 8 8 8 ==3
4 6 4 8  4 4 4 ==5 
4 3 4 4  4 4 4 ==2 
4 4 4 4  4 4 4 == 1

1 1 3 1 1 1 
1 1 4 1 1 1 ==1 
1 1 2 1 1 1== 1
1 1 1 1 1 1 == 1

1 4 2 
2 4 2 == 1
2 2 2 == 1 

5 2 6 10 3 9 2 

