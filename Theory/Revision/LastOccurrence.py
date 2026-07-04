arr=[5,3,2,7,5,2,0,8,5,1]
# Find the target number index which is at last position of its repetition 
#This method was related to max numbers 
target=int(input())
maxi=0
for i in range(len(arr)):
    if arr[i]==target:
        maxi=max(maxi,i+1)
print(maxi)