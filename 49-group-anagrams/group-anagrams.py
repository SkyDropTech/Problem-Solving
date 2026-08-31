class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={} 
        for x in strs:
            keys=("".join(sorted(x)))
            if keys not in mp:
                mp[keys]=[] 
            mp[keys].append(x)
        return list(mp.values())