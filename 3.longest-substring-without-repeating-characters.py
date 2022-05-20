#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        if len(s)==len(set(s)):
            return len(s)
        l=0
        ss=s[0]
        f=0
        for i in range(1,len(s)):
            l1=0
            if s[i] not in ss:
                ss=s[f:i+1]
            else:
                l1=i-f
                if l1>l:
                    l=l1
                f=s.index(s[i],f)+1
                ss=s[f:i+1]
        l1=i-f+1
        if l1>l:
            l=l1
        return l
                

# @lc code=end

