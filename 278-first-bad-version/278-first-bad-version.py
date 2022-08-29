# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        mid=0
        while l!=r:
            mid = (l+r)//2
            if not isBadVersion(mid):
                l=mid
            else:
                r=mid
            if l==r:
                return l
            elif l==r-1:
                return l if isBadVersion(l) else r
        return n