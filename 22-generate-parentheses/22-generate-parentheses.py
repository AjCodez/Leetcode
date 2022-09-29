from itertools import permutations 
class Solution:
#     l=[]
#     def isValid(self, s: str) -> bool:
#         st= []
#         if len(s)%2!=0:
#             return False
#         for i in s:
#             if i=='(' or i=='[' or i== '{':
#                 st.append(i)
#             elif i==')':
#                 if len(st)==0 or st[-1]!='(':
#                     return False
#                 else:
#                     st.pop()
#             elif i=='}':
#                 if len(st)==0 or st[-1]!='{':
#                     return False
#                 else:
#                     st.pop()
#             elif i==']':
#                 if len(st)==0 or st[-1]!='[':
#                     return False
#                 else:
#                     st.pop()
#         if len(st)!=0:
#             return False
#         else:
#             return True
#     def generateParenthesis(self, n: int) -> List[str]:
#         s='()'*n
#         self.perm(s,"")
#         l=[]
#         for i in self.l:
#             if self.isValid(i):
#                 l.append(i)
#         return l
#     def perm(self,q,s):
#         if len(q)==0:
#             self.l.append(s)
#             return
#         for i in range(len(q)):
#             c=q[i]
            
#             s1=s[0:i]
#             s2=s[i+1:]
            
#             self.perm(s1+s2,s+c)

    def generateParenthesis(self, n: int) -> List[str]:
        def gen(l,s,o,c):
            if len(s)==n*2:
                l.append(s)
                return
            if o<n:
                gen(l,s+'(',o+1,c)
            if c<o:
                gen(l,s+')',o,c+1)
        l=[]
        gen(l,"",0,0)
        return l