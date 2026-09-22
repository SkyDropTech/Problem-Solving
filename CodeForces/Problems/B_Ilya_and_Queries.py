s=input() 
m=int(input()) 
arr=[]
for i in range(m):
    l,r=map(int,input().split()) 
    arr.append([l,r])
for i in range(len(arr)):
    left=arr[i][0] 
    right=arr[i][1]
    ct=0
    while left<right:
        if s[left-1]==s[left]:
            ct+=1 
        left+=1 
    print(ct)