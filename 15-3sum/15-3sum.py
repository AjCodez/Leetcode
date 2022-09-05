# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         lis=set()
#         nums.sort()
#         for i in range(len(nums)-2):
#             l=i+1
#             r=len(nums)-1
#             while l<r:
#                 if nums[i]+nums[l]+nums[r]==0:
#                     # r-=1
#                     lis.add([nums[i],nums[l],nums[r]])
#                     a=int(nums[r])
#                     while nums[r]==a and r>l:
#                         r-=1
#                 elif nums[i]+nums[l]+nums[r]>0:
#                     a=int(nums[r])
#                     while nums[r]==a and r>l:
#                         r-=1
#                 else:
#                     a=int(nums[l])
#                     while nums[l]==a and l<r:
#                         l+=1
        
#         return list(lis)

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        counter = {}
        for i in nums:
            if i not in counter:
                counter[i] = 0    
            counter[i] += 1

        nums = sorted(counter)
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        output = []
        for i in range(len(nums)-1):
            # search range
            twoSum = -nums[i]
            min_half, max_half = twoSum - nums[-1], twoSum / 2
            l = bisect_left(nums, min_half, i + 1)
            r = bisect_left(nums, max_half, l)
            
            for j in nums[l:r]:
                if twoSum - j in counter:
                    output.append([nums[i], j, twoSum - j])

        for k in counter:
            if counter[k] > 1:
                if k == 0 and counter[k] >= 3:
                    output.append([0, 0, 0])
                elif k != 0 and -2 * k in counter:
                    output.append([k, k, -2 * k])
        return output