class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            min_len = len(prefix)
            if len(prefix) > len(strs[i]):
                prefix = prefix[:len(strs[i])]
                min_len = len(strs[i])
            
            for k in range(min_len):
                if prefix[k] != strs[i][k]:
                    prefix = prefix[:k]
                    break
            
            if len(prefix) == 0:
                break
        
        return prefix