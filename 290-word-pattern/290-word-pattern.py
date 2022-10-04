class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        rslt = True
        word_d = dict()
        
        lst = s.split(' ')
        
        if len(lst) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            p = pattern[i]
            if p in word_d:
                if word_d[p] != lst[i]:
                    rslt = False
                    break
            else:
                if lst[i] in word_d.values():
                    rslt = False
                    break
                else:
                    word_d[p] = lst[i]
                
        return rslt
        