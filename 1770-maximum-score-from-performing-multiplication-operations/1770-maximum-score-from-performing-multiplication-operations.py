class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n=len(nums)
        m=len(multipliers)
        
        dp=[[0] * (m+1) for i in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(m-1, -1, -1):
                
                r=n-(j-i)-1
                
                if r<0 or r>=n:
                    break
                
                s=nums[i]*multipliers[j]+dp[i+1][j+1]
                e=nums[r]*multipliers[j]+dp[i][j+1]
                dp[i][j]=max(s, e)
                
        return dp[0][0]

