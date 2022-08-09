class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        s_idx = 0
        
        for i in range(len(t)):
            if s_idx >= len(s):
                break
            
            if t[i] == s[s_idx]:
                s_idx += 1
            
            
        
        if s_idx >= len(s):
            return True
        else:
            return False
        