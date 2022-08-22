class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0 or n==2:
            return False
        if n==1:
            return True
        b=str(bin(n))[2:]
        if b[0]=='1' and b.count('0')%2==0 and b.count('1')==1:
            return True
        return False