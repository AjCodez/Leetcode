class Solution:
    def isPossible(self, nums: List[int]) -> bool:
#         TLE solution
        # l=[]
        # for i in nums:
        #     if not l:
        #         l.append([i])
        #         continue
        #     k=[]
        #     for j in l:
        #         if j[-1]==i-1:
        #             if len(j)<3:
        #                 j.append(i)
        #                 break
        #             else:
        #                 k=j
        #         # else:
        #         #     l.append([i])
        #         #     break
        #     else:
        #         if k:
        #             k.append(i)
        #         else:
        #             l.append([i])
        # for i in l:
        #     if len(i)<3:
        #         return False
        # return True
        
        cm=Counter(nums)
        hm=defaultdict(int)
        for i in range(len(nums)):
            if cm[nums[i]]==0:
                continue
            if hm[nums[i]]>0:
                hm[nums[i]]-=1
                hm[nums[i]+1]+=1
                cm[nums[i]]-=1
            elif cm[nums[i]]>0 and cm[nums[i]+1]>0 and cm[nums[i]+2]>0:
                cm[nums[i]]-=1
                cm[nums[i]+1]-=1
                cm[nums[i]+2]-=1
                hm[nums[i]+3]+=1
            else:
                return False
        return True