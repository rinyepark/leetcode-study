class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        cnt = [0,0,0]
        for i in nums:
            cnt[i] += 1
        
        idx = 0
        for i in range(len(cnt)):
            for k in range(cnt[i]):
                nums[idx] = i
                idx += 1
            
        
            