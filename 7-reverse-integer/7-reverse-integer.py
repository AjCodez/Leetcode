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
