class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        answer = True
        word_dict = dict()
        
        for i in range(len(t)):
            
            if s[i] not in word_dict:
                if t[i] in word_dict.values():
                    answer = False
                    break
                else:
                    word_dict[s[i]] = t[i]
            else:
                if word_dict[s[i]] != t[i]:
                    answer = False
                    break
        
        return answer
            