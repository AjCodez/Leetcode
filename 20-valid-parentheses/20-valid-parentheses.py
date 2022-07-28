class Solution:
    def isValid(self, s: str) -> bool:
        st= []
        if len(s)%2!=0:
            return False
        for i in s:
            if i=='(' or i=='[' or i== '{':
                st.append(i)
            elif i==')':
                if len(st)==0 or st[-1]!='(':
                    return False
                else:
                    st.pop()
            elif i=='}':
                if len(st)==0 or st[-1]!='{':
                    return False
                else:
                    st.pop()
            elif i==']':
                if len(st)==0 or st[-1]!='[':
                    return False
                else:
                    st.pop()
        if len(st)!=0:
            return False
        else:
            return True