n,m,a,b=map(int,input().split())
cost1=n*a
cost2=(n//m)*b + (n%m)*a
cost3=((n+m-1)//m)*b
print(min(cost1,cost2,cost3))