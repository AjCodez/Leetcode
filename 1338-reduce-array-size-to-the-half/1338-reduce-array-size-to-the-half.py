class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        m=Counter(arr)
        # for i in arr:
        #     if i in m:
        #         m[i]+=1
        #     else:
        #         m[i]=1
        l=list(m.values())
        # for i in m:
        #     l.append(m[i])
        l.sort()
        length=len(arr)-l[-1]
        c=1
        for i in range(len(l)-2,0,-1):
            if length<=len(arr)//2:
                return c
            else:
                length-=l[i]
                c+=1
        return c