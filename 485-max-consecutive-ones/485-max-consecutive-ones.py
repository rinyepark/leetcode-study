class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        l_str = ''.join([str(num) for num in nums])
        lst = l_str.split('0')
        
        max_l = 0
        for i in lst:
            if max_l < len(i):
                max_l = len(i)
        return max_l