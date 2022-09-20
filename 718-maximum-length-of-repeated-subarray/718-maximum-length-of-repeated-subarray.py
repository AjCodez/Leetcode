class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        s1 = ''.join([chr(i) for i in nums2])
            
        s = ''
        res = 0
        for c in nums1:
            s+=chr(c)
            if s in s1:
                res = max(res,len(s))
            else:
                s = s[1:]

        return res