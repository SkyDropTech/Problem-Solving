s=input().lower() 
name="hello" 
count=0 
for ch in s:
    if ch==name[count]:
        count+=1 
    if count==len(name):
        break 
if count==len(name):
    print("YES")
else:
    print("NO")