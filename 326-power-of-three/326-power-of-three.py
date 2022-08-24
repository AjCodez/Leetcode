class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        a = math.log(n)//math.log(3)
        b = math.ceil(math.log(n)/math.log(3))
        if 3**a==n or 3**b==n:
            return True
        return False