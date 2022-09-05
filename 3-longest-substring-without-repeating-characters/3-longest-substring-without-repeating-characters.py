class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        
        if len(s) > 0:
            max_len = 1
            
        for i in range(len(s)):
            idx = i + 1
            tmp = s[i]
            
            while idx < len(s):
                if s[idx] in tmp:
                    break
                tmp += s[idx]
                idx += 1
            if max_len < len(tmp):
                max_len = len(tmp)          
                
        return max_len