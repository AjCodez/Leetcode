class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)>len(haystack):
            return -1
        elif len(needle)==len(haystack):
            if needle==haystack:
                return 0
            else:
                return -1
        elif needle not in haystack:
            return -1
        d=len(haystack)-len(needle)
        for i in range(d+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
