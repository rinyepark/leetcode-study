class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        stack = [[]]
        for i in range(len(nums)):
            
            new_stack = []
            while stack:
                lst = stack.pop()
                
                new_stack.append(lst)
                
                tmp_lst = lst[:]
                tmp_lst.append(nums[i])
                new_stack.append(tmp_lst)
                
            stack = new_stack[:]
            
        return stack
            
            