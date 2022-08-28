class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        l=len(mat)-1
        r=0
        tl=0
        tr=len(mat)-1
        f=True
        while l!=0 or tl!=len(mat[0])-1 or tr!=0 or r!=len(mat[0])-1:
            diag = []
            t1=l
            t2=tl
            while t1<=tr+1 and t2<=r:
                diag.append(mat[t1][t2])
                t1+=1
                t2+=1
            t=0
            t1=l
            t2=tl
            diag.sort()
            while t1<=tr and t2<=r:
                mat[t1][t2]=diag[t]
                t+=1
                t1+=1
                t2+=1
            if l!=0:
                l-=1
            else:
                tl+=1
            if r!=len(mat[0])-1:
                r+=1
            else:
                tr-=1
        return mat