#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:

    def palindrome(s: str) -> bool:
        ss=s[::-1]
        if s==ss:
            return True
        return False

    def isPalindrome(self, x: int) -> bool:
        if x<0 or str(x)[len(str(x))-1]==0:
            return False 
        s=str(x)
        if Solution.palindrome(s):
            return True
        else:
            return False
        
# @lc code=end

