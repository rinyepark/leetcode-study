class Solution:
    def isHappy(self, n: int) -> bool:
        
        answer = False
        num_list = [n]
        
        while True:
            list_n = list(map(lambda x: int(x), list(str(n))))
            
            num = 0
            for i in list_n:
                num += i ** 2
            
            
            if num == 1:
                answer = True
                break
            if num in num_list:
                break
            
            num_list.append(num)
            n = num
        
        return answer
        
        
            
        