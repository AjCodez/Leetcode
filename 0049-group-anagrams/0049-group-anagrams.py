class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        l=[]
        
        for i in strs:
            temp=''.join(sorted(i))
            if temp in d:
                d[temp].append(i)
            else:
                d[temp]=[i]
        
        for i in d:
            l.append(d[i])
        return l