class Solution:
    def isUgly(self, n: int) -> bool:
        if n<1:
            return False
        i=2
        while n!=1:
            if i>5:
                return False
            while n%i==0:
                n=n//i
            i+=1
        return True