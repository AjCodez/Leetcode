class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr2=[""]
        
        m=0
        for i in arr:
            for j in arr2:
                temp=i+j
                if len(temp)!=len(set(temp)):
                    continue
                arr2.append(temp)
                m=max(m,len(temp))
        return m