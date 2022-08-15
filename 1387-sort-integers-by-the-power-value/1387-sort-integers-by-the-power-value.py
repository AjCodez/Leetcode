class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr=[]
        for i in range(lo,hi+1):
            st=0
            x=int(i)
            while x!=1:
                if x%2==0:
                    x=x//2
                else:
                    x=3*x+1
                st+=1
            arr.append((st,i))
        arr.sort()
        return arr[k-1][1]