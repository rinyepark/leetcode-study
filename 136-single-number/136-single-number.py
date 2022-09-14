class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        lst = list(set(nums))
        
        for i in lst:
            if nums.count(i) == 1:
                answer = i
                break
            
        return answer
        