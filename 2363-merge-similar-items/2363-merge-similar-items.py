class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d={}
        for i,j in items1:
            d[i] = j
        for i,j in items2:
            if i in d:
                d[i]+=j
            else:
                d[i]=j
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort(key=lambda x:x[0])
        
        return l