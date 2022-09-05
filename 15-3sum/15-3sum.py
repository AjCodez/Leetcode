class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lis=[]
        nums.sort()
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[i]+nums[l]+nums[r]==0:
                    # r-=1
                    if [nums[i],nums[l],nums[r]] not in lis:
                        lis.append([nums[i],nums[l],nums[r]])
                    a=int(nums[r])
                    while nums[r]==a and r>l:
                        r-=1
                elif nums[i]+nums[l]+nums[r]>0:
                    a=int(nums[r])
                    while nums[r]==a and r>l:
                        r-=1
                else:
                    a=int(nums[l])
                    while nums[l]==a and l<r:
                        l+=1
        
        return lis