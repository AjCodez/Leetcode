#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s=str(x)[1:]
            s=s[::-1]
            s=int(s)
            s=0-s 
            if s<(-2**31):
                s=0
            return s
        s=str(x)
        s=s[::-1]
        s=int(s)
        if s>(2**31):
            s=0
        return s

# @lc code=end

