class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        answer = list(map(lambda x: x**2, nums))
        answer.sort()
        
        return answer
        