class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        lst = []
        twice = []
        
        for i in nums:
            if i not in lst:
                lst.append(i)
            else:
                if i not in twice:
                    twice.append(i)
                    
        answer = list(set(lst) - set(twice))[0]
            
        return answer
        