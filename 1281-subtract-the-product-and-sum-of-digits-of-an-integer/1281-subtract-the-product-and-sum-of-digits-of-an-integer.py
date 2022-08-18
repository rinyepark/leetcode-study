class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        lst = list(map(lambda x: int(x), str(n)))
        
        answer = 1
        for i in lst:
            answer *= i
        
        return answer - sum(lst)
        