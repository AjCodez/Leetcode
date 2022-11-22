class Solution:
    def numSquares(self , n):
        if math.isqrt(n)**2 == n: 
            return 1
        for i in range(1,math.isqrt(n)+1):
            if (k := n - i**2) == math.isqrt(k)**2:
                return 2
        while n % 4 == 0:
            n /= 4
        if n%8!=7: 
            return 3
        return 4     