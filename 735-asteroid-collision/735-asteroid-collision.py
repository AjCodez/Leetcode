class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        st=[]
        for i in asteroids:
            if not st:
                st.append(i)
            elif (i<0 and st[-1]<0) or (i>0 and st[-1]>0) or (st[-1]<0 and i>0):
                st.append(i)
            else:
                while st and st[-1]>0 and abs(i)>st[-1]:
                    st.pop()
                if not st:
                    st.append(i)
                elif st[-1]==-i:
                    st.pop()
                elif (i<0 and st[-1]<0) or (i>0 and st[-1]>0) or (st[-1]<0 and i>0):
                    st.append(i)
        return st
                        
        
        # stp=[]
        # stn=[]
        # for i in asteroids:
        #     if i>0:
        #         stp.append(i)
        #     else:
        #         stn.append(i)
        #     while stn and stp:
        #         p=stp[-1]
        #         n=stn[-1]
        #         if p>abs(n):
        #             stn.pop()
        #         elif abs(n)>p:
        #             stp.pop()
        #         else:
        #             stn.pop()
        #             stp.pop()
        # while stp and stn:
        #     if p>abs(n):
        #         stn.pop()
        #     elif abs(n)>p:
        #         stp.pop()
        # if stp:
        #     return stp
        # elif stn:
        #     return stn
        # else:
        #     return []