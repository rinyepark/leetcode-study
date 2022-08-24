class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        
        target_idx = len(nums)-3
        while target_idx >= 0:
            max_arr = nums[target_idx:target_idx+3]
            sum_arr = sum(max_arr)
            if sum_arr - max_arr[-1] > max_arr[-1]:
                answer = sum_arr
                break
            target_idx -= 1
        return answer
            
        
        