class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l=[]

        def comb(arr,i):
            l.append(arr.copy())
            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                arr.append(nums[j])
                comb(arr,j+1)
                arr.pop()
        
        nums.sort()
        comb([],0)
        return l