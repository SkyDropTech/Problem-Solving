arr=list(map(int,input().split()))
k=int(input())
k=k%len(arr)
temp=[] 

for i in range(k,len(arr)):
    temp.append(arr[i])
for i in range(k):
    temp.append(arr[i])
print(temp)
