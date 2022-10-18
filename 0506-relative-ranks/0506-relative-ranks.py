class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        medal = {"1":"Gold Medal", "2": "Silver Medal", "3": "Bronze Medal"}
        sort_score = sorted(score, reverse=True)
        
        answer = ['' for i in range(len(score))]
        
        for i in range(len(score)):
            idx = sort_score.index(score[i])
            
            out = str(idx+1)
            if out in medal:
                answer[i] = medal[out]
            else:
                answer[i] = out
        
        return answer