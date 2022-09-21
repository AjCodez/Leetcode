class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = 0
        l=[]
        for i in nums:
            if i%2==0:
                sums+=i
        for i,j in queries:
            if nums[j]%2==0:
                sums-=nums[j]
            nums[j]+=i
            if nums[j]%2==0:
                sums+=nums[j]
            l.append(sums)
        return l
    