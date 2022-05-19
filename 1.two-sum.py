#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b=0
        e=len(nums)-1
        l=[(v,ind) for ind,v in enumerate(nums)]
        l.sort()

        while b<e:
            s = l[b][0]+l[e][0]
            if s>target:
                e=e-1
            elif s<target:
                b=b+1
            else:
                r=[l[b][1],l[e][1]]
                return r 
        
# @lc code=end

