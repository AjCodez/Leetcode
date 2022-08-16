class Solution:
    def firstUniqChar(self, s: str) -> int:
        dp1={}
        dp2={}
        for i in range(len(s)):
            if s[i] in dp1:
                if s[i] in dp2:
                    dp2.pop(s[i])
            else:
                dp1[s[i]]=i
                dp2[s[i]]=i
        if not dp2:
            return -1 
        return dp2[list(dp2.keys())[0]]