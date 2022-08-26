class Solution:
    # def check(self,n):
    #     if n&(n-1)==0:
    #         return True
    #     return False
    def reorderedPowerOf2(self, n: int) -> bool:
        # c=Counter(str(n))
        a=sorted(str(n))
        for i in range(32):
            b=sorted(str(2**i))
            # if Counter(str(2**i))==c:
            if a==b:
                return True
        return False