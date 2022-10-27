class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        d={}
        a=[]
        b=[]
        
        for i in range(len(img1)):
            for j in range(len(img1)):
                if img1[i][j]==1:
                    a.append((i,j))
                if img2[i][j]==1:
                    b.append((i,j))
        n=0
        for i in a:
            for j in b:
                k=(i[0]-j[0],i[1]-j[1])
                if k in d:
                    d[k]+=1
                else:
                    d[k]=1
                n=max(n,d[k])
        return n