class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        odd_high = high % 2 == 1
        odd_low = low % 2 == 1
        
        answer = 0
        if odd_high or odd_low:
            answer += (high-low)//2 + 1
        else:
            answer += (high-low)//2
        
            
        return answer