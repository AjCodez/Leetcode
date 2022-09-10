class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        mb=prices[0]
        ms=prices[0]
        i=0
        j=0
        for k in range(len(prices)):
            if prices[k]<mb:
                mb=prices[k]
                i=k
            if j<=i:
                ms=prices[k]
                j=k
            else:
                ms=max(prices[k],ms)
                j=k
            m=max(m,ms-mb)
        return m
        