class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        an_dict = {}
        
        while strs:
            x = strs.pop()
            
            sort_x = ''.join(sorted(x))
            if sort_x in an_dict:
                an_dict[sort_x].append(x)
            else:
                an_dict[sort_x] = [x]
                
        for i in an_dict.values():
            answer.append(i)
        
        return answer