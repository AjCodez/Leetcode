class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums=nums1[:m]
        nums1.clear()
        m1=0
        n1=0
        while m1<m and n1<n:
            if nums[m1]<nums2[n1]:
                nums1.append(nums[m1])
                m1+=1
            else:
                nums1.append(nums2[n1])
                n1+=1
        while m1<m:
            nums1.append(nums[m1])
            m1+=1
        while n1<n:
            nums1.append(nums2[n1])
            n1+=1
            