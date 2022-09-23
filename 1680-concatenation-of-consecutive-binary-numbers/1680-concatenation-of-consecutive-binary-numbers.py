class Solution:
    def concatenatedBinary(self, n: int, s='') -> int:
        s=''
        for i in range(1,n+1):
            s+=str(bin(i))[2:]
            
        return int(s,2)%(10**9+7)