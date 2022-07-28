class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        f1=0
        if len(needle)>len(haystack):
            return -1
        elif len(needle)==len(haystack):
            if needle==haystack:
                return 0
            else:
                return -1
        if needle not in haystack:
            return -1
        while f1!=len(haystack):
            f2=f1+1
            ss=haystack[f1:f2]
            while ss in needle:
                if ss==needle:
                    return f1
                elif f1==len(haystack)-1:
                    return -1
                else:
                    f2+=1
                    ss=haystack[f1:f2]
                    
            f1+=1
        else:
            return -1