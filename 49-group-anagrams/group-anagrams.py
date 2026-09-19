class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n=len(strs)
        arr=[0]*n
        freq={}
        for i in range(len(strs)):
            arr[i]="".join(sorted(strs[i]))
            if arr[i] not in freq:
                freq[arr[i]]=[]
            freq[arr[i]].append(strs[i])
        return list(freq.values())