class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        answer = []
        if len(nums) > 0:
            nums.append(nums[-1])
        
        beg = ""
        cur = ""
        for i in range(len(nums)):
            if type(beg) == str:
                beg = nums[i]
                cur = beg
            
            else:
                if cur + 1 != nums[i]:
                    if cur == beg:
                        answer.append(str(beg))
                    else:
                        answer.append(str(beg) + "->" + str(cur))
                    
                    beg = nums[i]
                    cur = beg
                else:
                    cur = nums[i]
    
        
        return answer
                
                