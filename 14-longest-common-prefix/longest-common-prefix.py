class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        pr=strs[0]
        for i in range(1,len(strs)):
            while strs[i].find(pr) != 0:
                pr=pr[:-1]
                if pr=="":
                    return ""
        return pr