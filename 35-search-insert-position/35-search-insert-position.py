class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = len(nums)
        for i in range(len(nums)):
            if target <= nums[i]:
                answer = i
                break
        return answer