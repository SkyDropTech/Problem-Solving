t=int(input())
for _ in range(t):
    n=int(input())
    a=list(int,input().split())
    for i in range(n-1):
        if (a[i]%2)==(a[i+1]%2):
            break 
        else:
            