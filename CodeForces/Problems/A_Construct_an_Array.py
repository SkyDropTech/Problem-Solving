t=int(input())
for _ in range(t):
    n=int(input())
    lst=[]
    for i in range(1,n*2,2):
        lst.append(i) 
    print(*lst)
print()