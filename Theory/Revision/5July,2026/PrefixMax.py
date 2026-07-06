arr=list(map(int,input().split()))
tar=[0]*len(arr)
tar[0]=arr[0] 
for i in range(1,len(arr)):
    tar[i]=max(arr[i],tar[i-1])
print(tar)