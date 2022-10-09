class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_lst = [0 for i in range(26)]
        t_lst = [0 for i in range(26)]
        
        for i in range(len(s)):
            s_lst[ord(s[i])-97] += 1
            t_lst[ord(t[i])-97] += 1
        
        t_lst[ord(t[-1])-97] += 1
        
        for i in range(26):
            if s_lst[i] != t_lst[i]:
                return chr(i+97)
        
        