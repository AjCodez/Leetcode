class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s,e=-1,0
        try:
            s=nums.index(target)
            if s==len(nums)-1:
                return [s,s]
            e=s
            while nums[e]==target:
                e+=1
            return [s,e-1]
        except:
            return [s,e-1]