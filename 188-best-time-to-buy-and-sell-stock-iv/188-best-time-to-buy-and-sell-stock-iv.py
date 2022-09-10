class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices)<=1 or k<=0:
            return 0
        if k>=len(prices)//2:
            p=0
            for i in range(len(prices)-1):
                if prices[i+1]>prices[i]:
                    p+=prices[i+1]-prices[i]
            return p
        b=[-math.inf]*k
        s=[0]*k
        for i in range(len(prices)):
            for j in range(k):
                b[j]=max(b[j],0-prices[i] if j==0 else s[j-1]-prices[i])
                s[j]=max(s[j],b[j]+prices[i])
        return s[-1]