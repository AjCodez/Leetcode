class Solution:
    def reverseWords(self, s: str) -> str:
        ss=''
        sss=''
        for i in s:
            if i==' ':
                ss+=sss+' '
                sss=''
            else:
                sss=i+sss
        
        return ss+sss