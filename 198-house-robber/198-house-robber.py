class Solution:
    
    def rob(self, nums: List[int]) -> int:
        a,b,c,d=0,0,0,0
        for i in range(len(nums)):
            c=max(a,b)
            d=max(a+nums[i],b)
            a=c
            b=d
        return max(c,d)