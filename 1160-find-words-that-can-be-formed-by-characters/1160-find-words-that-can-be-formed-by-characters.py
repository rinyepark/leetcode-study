class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        answer = 0
        cd = dict()
        for i in chars:
            if i not in cd:
                cd[i] = 1
            else:
                cd[i] += 1
        
        for i in words:
            cd_copy = cd.copy()
            flag = True
            for k in i:
                if k in cd_copy:
                    cd_copy[k] -= 1
                    if cd_copy[k] < 0:
                        flag = False
                        break
                else:
                    flag = False
                    break
            if flag:
                answer += len(i)
        
        return answer
            