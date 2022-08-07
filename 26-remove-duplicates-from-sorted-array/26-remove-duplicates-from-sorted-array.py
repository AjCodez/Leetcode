class Solution:
    def removeDuplicates(self, nums) -> int:
        c=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==c:
                nums[i]='_'
            else:
                c=nums[i]
        for i in range(nums.count('_')):
            nums.remove('_')
        return len(nums)