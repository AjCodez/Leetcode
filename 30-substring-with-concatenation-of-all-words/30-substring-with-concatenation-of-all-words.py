class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans=[]
        l=len(words[0])
        dp={}
        for i in words:
            if i in dp:
                dp[i]+=1
            else:
                dp[i]=1
        for i in range(len(s)):
            if len(s[i:])<(len(words)*l):
                break
            words2=dp.copy()
            j=i
            while s[i:i+l] in words2:
                words2[s[i:i+l]]-=1
                if words2[s[i:i+l]]==0:
                    words2.pop(s[i:i+l])
                i+=l
            if not words2:
                ans.append(j)
        return ans