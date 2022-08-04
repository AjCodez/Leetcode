# class Solution:
#     def subarraysDivByK(self, nums: List[int], k: int) -> int:
#         c=0
#         for i in range(len(nums)):
#             for j in range(i,len(nums)):
#                 s=sum(nums[i:j+1])
#                 if s%k==0:
#                     c+=1
#         return c

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        d = [1] + [0] * K 
        acc = 0
        for a in A:
            acc = (acc + a) % K 
            if d[acc]:
                res += d[acc]
            d[acc] += 1            
        return res