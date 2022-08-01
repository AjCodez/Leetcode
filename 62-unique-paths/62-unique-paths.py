class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m==0 or n==0:
            return 1
        m-=1
        n-=1
        if m<n:
            m,n=n,m
        res=1
        i=1
        for j in range(m+1,m+n+1):
            res*=j
            res/=i
            i+=1
        return int(res)