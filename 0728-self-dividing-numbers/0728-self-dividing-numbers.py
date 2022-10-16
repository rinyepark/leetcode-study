class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        
        for i in range(left, right+1):
            str_num = str(i)
            flag = True
            for s in str_num:
                if s == '0' or i % int(s) != 0:
                    flag = False
                    break
            
            if flag:
                answer.append(i)
        
        
        return answer