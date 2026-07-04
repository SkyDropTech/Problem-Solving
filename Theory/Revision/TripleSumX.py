arr=list(map(int,input().split()))
arr.sort()
X=int(input())
ok=False
for i in range(len(arr)-2):
    l=i+1
    r=len(arr)-1 
    while l<r:
        total=arr[i]+arr[l]+arr[r]
        if total==X:
            print("Found")
            ok=True 
            break 
        elif total<X:
            l+=1 
        else:
            r-=1 
if not ok:
    print("Nothing is there")
