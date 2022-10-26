class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l=[]

        def comb(arr,s,i):
            if s==target:
                l.append(arr.copy())
                return
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if s+candidates[j]>target:
                    break
                arr.append(candidates[j])
                s+=candidates[j]
                comb(arr,s,j+1)
                s-=arr.pop()
        candidates.sort()
        comb([],0,0)
        return l