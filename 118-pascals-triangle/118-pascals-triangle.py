class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p=[]
        for i in range(numRows):
            l=[]
            for j in range(i+1):
                if j==0 or j==i:
                    l.append(1)
                elif i==2:
                    l.append(2)
                else:
                    l.append(p[i-1][j]+p[i-1][j-1])
            p.append(l)
        return p