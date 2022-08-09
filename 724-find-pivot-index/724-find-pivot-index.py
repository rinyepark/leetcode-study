class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        answer = -1
        
        pivot_idx = 0
        
        l_sum = 0
        r_sum = sum(nums[1:])
        for i in range(len(nums)):
            if l_sum == r_sum:
                answer = pivot_idx
                break
            else:
                pivot_idx += 1
                if pivot_idx >= len(nums):
                    break
                l_sum += nums[pivot_idx-1]
                r_sum -= nums[pivot_idx]
            
            
        return answer
            