class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self.comb(m+n-2,n-1)
    def comb(self,a,b):
        res=1
        for i in range(b+1,a+1):
            res = (res*i)/(i-b)
        return int(res)