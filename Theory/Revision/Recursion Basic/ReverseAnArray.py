arr=[0,1,2,3,4,5,6,7] 
def val(arr,left,right):
    if left>=right:
        return 
    arr[left],arr[right]=arr[right],arr[left] 
    return val(arr,left+1,right-1) 
val(arr,2,6)
print(arr)