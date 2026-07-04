arr=[0,1,0,3,1,2]
i=0 
for j in range(1,len(arr)):
    if arr[i]==0 and arr[j]>0:
        arr[i],arr[j]=arr[j],arr[i] 
        i+=1 
print(arr)

