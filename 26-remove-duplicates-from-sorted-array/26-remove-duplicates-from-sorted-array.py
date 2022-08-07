class Solution:
    def removeDuplicates(self, nums) -> int:
        c=nums[0]
        j=1
        for i in range(1,len(nums)):
            if nums[i]!=c:
                c=nums[i]
                nums[j]=nums[i]
                j+=1
        return j
    
    
