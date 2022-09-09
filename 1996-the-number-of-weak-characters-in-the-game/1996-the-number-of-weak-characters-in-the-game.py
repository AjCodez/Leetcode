class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        p.sort(key = lambda x: (-x[0],x[1]))
        
        c=0
        m=0
        for i,j in p:
            if j<m:
                c+=1
            else:
                m=j
        return c