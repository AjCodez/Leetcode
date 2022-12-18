class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        # ind1={0:temperatures[0]}
        # for i in range(1,len(temperatures)):
        #     for j in list(ind1):
        #         if temperatures[i]>ind1[j]:
        #             ans[j]=i-j
        #             ind1.pop(j)
        #     ind1[i]=temperatures[i]
        # return ans
        
        st=[]
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]]<temperatures[i]:
                curr=st.pop()
                ans[curr]=i-curr
            st.append(i)
        return ans