class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        m=0
        for i in range(n//2):
            m=max(m,nums[i]+nums[n-i-1])
            
        return m