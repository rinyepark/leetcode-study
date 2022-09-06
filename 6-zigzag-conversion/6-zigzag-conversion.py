class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = ['' for i in range(numRows)]
        
        idx = 0
        mode = 'u'
        # 00 0 0 
        # 0 1 0 1 
        # 0 1 2 1 0
        # 0 1 2 3 2 1 0
        for i in s:
            lst[idx] += i
            
            
            if mode == "u":
                idx += 1
            else:
                idx -= 1
            
            if mode == "u":
                if idx >= numRows:
                    mode = "d"
                    if idx - 2 < 0:
                        idx -= 1
                    else:
                        idx -= 2
            else:
                if idx < 0:
                    mode = "u"
                    if idx + 2 >= numRows:
                        idx += 1
                    else:
                        idx += 2
            
            
        return ''.join(lst)
                
            
            