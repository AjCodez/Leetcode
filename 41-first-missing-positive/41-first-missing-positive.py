class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num=set(nums)
        s=1
        while s in num:
            s+=1
        return s