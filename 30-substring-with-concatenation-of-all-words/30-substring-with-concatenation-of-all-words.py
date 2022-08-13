class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans=[]
        l=len(words[0])
        for i in range(len(s)):
            if len(s[i:])<(len(words)*l):
                break
            words2=list(words)
            j=i
            while s[i:i+l] in words2:
                words2.remove(s[i:i+l])
                i=i+l
            if not words2:
                ans.append(j)
                
        return ans