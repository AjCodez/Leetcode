class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        i=0
        sx=0
        sy=0
        l=[]
        for i in range(len(mat)+len(mat[0])-1):
            t=[]
            if i<len(mat[0]):
                sy=i
            else:
                sx+=1
            r,c=sx,sy
            while r<len(mat) and c>=0:
                t.append(mat[r][c])
                r+=1
                c-=1
            if i%2==0:
                l=l+t[::-1]
            else:
                l=l+t
        return l
    
    