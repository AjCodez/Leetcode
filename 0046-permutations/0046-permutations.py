class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        l=[]
        
        def perm(i,arr):
            if i==len(arr):
                l.append(arr.copy())
                return
            
            for j in range(i,len(arr)):
                arr[i],arr[j]=arr[j],arr[i]
                perm(i+1,arr)
                arr[i],arr[j]=arr[j],arr[i]
        
        perm(0,nums)
        return l