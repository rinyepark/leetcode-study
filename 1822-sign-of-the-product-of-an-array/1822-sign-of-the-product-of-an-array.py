class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        answer = 1
        for i in nums:
            if i == 0:
                return 0
            
            answer *= i//abs(i)
            
                
        return answer
            