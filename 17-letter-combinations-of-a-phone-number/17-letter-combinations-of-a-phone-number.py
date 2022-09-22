class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        phone = {'2':["a","b","c"], '3':["d","e","f"], 
                '4':["g","h","i"], '5': ["j","k","l"], '6':["m","n","o"],
                '7': ["p","q","r","s"], '8':["t","u","v"],'9':["w","x","y","z"]}
        
        
        lst = list(digits)
        
        if len(lst) > 0:
            answer = phone[lst[0]][:]
        
        for i in range(1, len(lst)):
            tmp = []
            tmp_lst = phone[lst[i]]
            
            while answer:
                x = answer.pop()
                
                for k in tmp_lst:
                    tmp.append(x + k)
                
            answer = tmp[:]           
            
        
        return answer
        
        
        
        
        