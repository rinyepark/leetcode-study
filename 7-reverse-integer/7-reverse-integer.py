class Solution:
    def reverse(self, x: int) -> int:
        s = list(str(x))
        
        idx= len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] != '0':
                idx = i
                break
        
        s = s[:idx+1]
        if s[0] == '-':
            rs = int('-' + ''.join(s[:0:-1]))
        else:
            rs = int(''.join(s[::-1]))
        
        
        if rs < pow(-2, 31) or rs > pow(2, 31) - 1:
            return 0
        else:
            return rs
        