class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer = True
        check = dict()
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in check:
                check[s[i]] += 1
            else:
                check[s[i]] = 1
        
            
            if t[i] in check:
                check[t[i]] -= 1
            else:
                check[t[i]] = -1
        
        

        for sd in check:
            if check[sd] != 0:
                answer = False
                break
        
        return answer
        