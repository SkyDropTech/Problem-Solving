arr=[4,5,1,3,8,6,2] 
target= 0
ok=False 
for i in range(len(arr)):
    if arr[i]==target:
        ok= True 
if ok:
    print("YES")
else:
    print("NO")
