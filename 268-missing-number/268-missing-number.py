class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=0
        num=set(nums)
        while n in num:
            n+=1
        return n