class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ans=0
        l=0
        r=len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m]<target:
                l=m+1
                ans=l
            else:
                r=m-1
                ans=r+1
        return ans