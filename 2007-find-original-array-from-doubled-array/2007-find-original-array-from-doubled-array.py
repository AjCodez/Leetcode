class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        changed.sort(key=lambda x:-x)
        l=[]
        s={}
        for i in changed:
            if i*2 in s:
                s[i*2]-=1
                if s[i*2]==0:
                    del s[i*2]
                l.append(i)
            elif i in s:
                s[i]+=1
            else:
                s[i]=1
        if s:
            return []
        return l