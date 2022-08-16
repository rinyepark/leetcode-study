class Solution:
    def search(self, nums: List[int], target: int) -> int:
        beg = 0
        end = len(nums)-1
        find_idx = -1
        while beg <= end:
            cur = (end - beg) // 2 + beg
            if nums[cur] > target:
                end = cur - 1
            elif nums[cur] < target:
                beg = cur + 1
            else:
                find_idx = cur
                break
        
        return find_idx