arr=list(map(int,input().split()))
freq={}
for i in arr:
    if i not in freq:
        freq[i]=1 
    else:
        continue
x=len(arr)-len(list(freq))
new_arr=list(freq)+["_"]*x
print(list(freq))
