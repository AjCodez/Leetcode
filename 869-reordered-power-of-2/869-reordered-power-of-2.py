class Solution:
    # def check(self,n):
    #     if n&(n-1)==0:
    #         return True
    #     return False
    def reorderedPowerOf2(self, n: int) -> bool:
        c=Counter(str(n))
        for i in range(32):
            n=2**i
            if Counter(str(n))==c:
                return True
        return False