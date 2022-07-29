class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def patternArray(s):
            d={}
            p=[]
            f=1
            for i in s:
                if i in d:
                    p.append(d[i])
                else:
                    d[i]=f
                    p.append(d[i])
                    f+=1
            return p
        arr = patternArray(pattern)
        ans=[]
        for i in words:
            tarr=patternArray(i)
            if tarr==arr:
                ans.append(i)
        return ans