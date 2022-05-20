#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1=len(nums1)
        l2=len(nums2)

        nums3=[0]*(l1+l2)

        i,j,k=0,0,0

        while i<l1 and j<l2:
            if nums1[i]<=nums2[j]:
                nums3[k]=nums1[i]
                i+=1
                k+=1
            else:
                nums3[k]=nums2[j]
                j+=1
                k+=1
        while i<l1:
            nums3[k]=nums1[i]
            i+=1
            k+=1
        while j<l2:
            nums3[k]=nums2[j]
            j+=1
            k+=1
        if len(nums3)%2!=0:
            return float(nums3[len(nums3)//2])
        else:
            return (nums3[(len(nums3)-1)//2]+nums3[(len(nums3)+1)//2])/2
# @lc code=end

