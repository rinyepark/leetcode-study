class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        answer = True
        s_dict = dict()
        
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        
        for k in t:
            if k in s_dict:
                s_dict[k] -= 1
                if s_dict[k] < 0:
                    answer = False
                    break
            else:
                answer = False
                break
        
        for sd in s_dict:
            if s_dict[sd] != 0:
                answer = False
                break
        
        return answer
        