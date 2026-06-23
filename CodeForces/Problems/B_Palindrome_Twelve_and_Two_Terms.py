t=int(input())

for _ in range(t):
    n=int(input())

    r=n%12

    if r==10:
        a=22
    else:
        a=r

    if a>n:
        print(-1)
    else:
        print(a,n-a)