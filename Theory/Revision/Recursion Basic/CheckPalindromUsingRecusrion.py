s="NITIN" 
n=len(s)
def palindrom(s,left,right):
    if left>=right:
        return True 
    if s[left]!=s[right]:
        return False 
    return palindrom(s,left+1,right-1) 
print(palindrom(s,0,n-1))