class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        d = dict()
        
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 0
        
        for i in d:
            if d[i] == 0:
                answer = i
                break
            
        return answer
        