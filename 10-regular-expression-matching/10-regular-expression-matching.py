class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        a=re.fullmatch(p,s)
        if a:
            return True
        return False