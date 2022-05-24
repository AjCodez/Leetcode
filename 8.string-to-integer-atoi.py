#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        if s=='':
            return 0
        s=s.strip()
        ss=''
        for i in range(len(s)):
            if s[i].isdigit():
                ss=ss+s[i]
            elif i==0:
                if s[i]=='-' or s[i]=='+':
                    ss=ss+s[i]
                else:
                    return 0
            else:
                if ss=='':
                    return 0
                else:
                    break
        try:
            n=int(ss)
        except:
            return 0
        if n>((2**31)-1):
            return (2**31)-1
        elif n<(-2**31):
            return -2**31
        else:
            return n
        
# @lc code=end

