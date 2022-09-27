class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unique_size = (len(nums) - 1)//3 + 1
        
        arr_d = dict()
        
        
        for i in range(len(nums)):
            if nums[i] in arr_d:
                arr_d[nums[i]] = False
            else:
                arr_d[nums[i]] = True
        
        for k in arr_d.keys():
            if arr_d[k]:
                return k