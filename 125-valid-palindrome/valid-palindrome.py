class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans="" 
        for i in s:
            if i.isalnum():
                ans+=i 
        ans=ans.lower()
        for i in range(len(ans)):
            if ans!=ans[::-1]:
                return False 
        return True


        