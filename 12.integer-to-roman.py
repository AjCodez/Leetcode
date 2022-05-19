#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        m=num//1000
        num=num%1000
        d=num//500
        num=num%500
        c=num//100
        num=num%100
        l=num//50
        num=num%50
        x=num//10
        num=num%10
        v=num//5
        num=num%5
        i=num

        s=''
        s=s+'M'*m
        if c+d==5:
            s=s+'CM'
        else:
            s=s+'D'*d
            if c==4:
                s=s+'CD'
            else:
                s=s+'C'*c
        if l+x==5:
            s=s+'XC'
        else:
            s=s+'L'*l
            if x==4:
                s=s+'XL'
            else:
                s=s+'X'*x
        if i+v==5:
            s=s+'IX'
        else:
            s=s+'V'*v
            if i==4:
                s=s+'IV'
            else:
                s=s+'I'*i
        return s

        
# @lc code=end