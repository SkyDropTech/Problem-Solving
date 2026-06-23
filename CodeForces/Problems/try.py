n = int(input())

if n <= 3:
    print(-1)
else:
    for i in range(3, n+1):
        print(i, end=" ")
    print(1, 2)
