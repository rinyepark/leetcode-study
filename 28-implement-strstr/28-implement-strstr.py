class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        answer = -1
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                answer = i
                break
        return answer