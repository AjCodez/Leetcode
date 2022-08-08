class Solution:
    # def big(self,cin,din,count,nums):
    #     if din==len(nums):
    #         return count
    #     if nums[cin]<nums[din]:
    #         return self.big(cin,din+1,count+1,nums)
    #     else:
    #         return self.big(cin,din+1,count,nums)
            
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==1 or len(set(nums))==1:
            return 1
        
        # c1=1
        # for i in range(len(nums)):
        #     c2=self.big(i,i+1,1,nums)
        #     if c2==len(nums):
        #         return len(nums)
        #     if c2>c1:
        #         c1=c2
        # return c1
        ss=[]
        for i in nums:
            
            if len(ss)==0 or ss[-1]<i:
                ss.append(i)
            else:
                index=bisect_left(ss,i)
                ss[index]=i
        return len(ss)