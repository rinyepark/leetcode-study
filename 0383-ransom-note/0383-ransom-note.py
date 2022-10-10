class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ran_lst = [0 for i in range(26)]
        
        for i in ransomNote:
            ran_lst[ord(i)-97] += 1
        
        for i in magazine:
            ran_lst[ord(i)-97] -= 1
        
        for i in ran_lst:
            if i > 0:
                return False
        
        return True
        