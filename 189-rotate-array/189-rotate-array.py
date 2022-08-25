class Solution:
    def rotatesubarr(self,nums, i, j):
        while i<j:
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp

            i+=1
            j-=1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        self.rotatesubarr(nums,0,len(nums)-k-1)
        self.rotatesubarr(nums,len(nums)-k,len(nums)-1)
        self.rotatesubarr(nums,0,len(nums)-1)
        
#         def rotatesubarr(nums, i, j):
#             while i<j:
#                 temp=nums[i]
#                 nums[i]=nums[j]
#                 nums[j]=temp
                
#                 i+=1
#                 j-=1
                