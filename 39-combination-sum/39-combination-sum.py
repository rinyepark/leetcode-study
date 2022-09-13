class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        answer = []
        
        stack = list(map(lambda x : [x], candidates))
        
        while stack:
            lst = stack.pop()
            sum_lst = sum(lst)
            
            if sum_lst == target:
                lst.sort()
                if lst not in answer:
                    answer.append(lst)
            elif sum_lst < target:
                for i in candidates:
                    tmp = lst[:]
                    if sum_lst + i <= target:
                        tmp.append(i)
                        stack.append(tmp)
            
        return answer
        