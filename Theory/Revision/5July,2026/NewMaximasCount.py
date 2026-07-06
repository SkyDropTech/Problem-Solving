arr=list(map(int,input().split()))
tar=[0]*len(arr)
maxi=arr[0] 
ct=1
for i in range(1,len(arr)):
    if arr[i]>maxi:
        maxi=arr[i]
        ct+=1 
        print(arr[i])
print(ct)