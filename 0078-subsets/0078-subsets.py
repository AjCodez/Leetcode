class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[]
        def subs(arr1, i, arr2):
            if i>=len(arr1):
                l.append(arr2.copy())
                return
            arr2.append(arr1[i])
            subs(arr1,i+1,arr2)
            arr2.pop()
            subs(arr1,i+1,arr2)
        subs(nums,0,[])
        return l