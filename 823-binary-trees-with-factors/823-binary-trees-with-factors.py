class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        dp={}
        for i in arr:
            count=1 
            for j in dp:
                if i%j==0 and i//j in dp:
                    count+=dp[j]*dp[i//j]
            dp[i]=count
        nobt=0
        for i in dp:
            nobt+=dp[i]
        return nobt % (10**9 + 7)