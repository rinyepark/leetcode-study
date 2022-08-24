class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        if 0 in nums:
            return 0
        
        answer = 1
        for i in nums:
            answer *= i//abs(i)
                
        return answer
            