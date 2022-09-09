class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = ['()', '{}', '[]']
        
        while len(s) > 0:
            s_clean = s
            for i in valid:
                s_clean = s_clean.replace(i, '')
            
            if len(s_clean) == len(s):
                break
            else:
                s = s_clean
        
        if len(s) > 0:
            return False
        return True
        
            
                
            