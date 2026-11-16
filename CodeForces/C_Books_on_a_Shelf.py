t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    lst=[0]*n
    for i in range(n):
        if i%2==0:
            lst[i//2]=nums[i]
        else:
            lst[n-1-(i//2)]=nums[i]      
    visible=set()
    maxi=0
    for i in range(n):
        if lst[i]>maxi:
            visible.add(i)
            maxi=lst[i]

    maxi=0
    for i in range(n-1,-1,-1):
        if lst[i]>maxi:
            visible.add(i)
            maxi=lst[i]

    print(len(visible))
    print(*lst)
    