class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a= Counter(ransomNote)
        for i in magazine:
            if i in a:
                a[i]-=1
                if a[i]==0:
                    a.pop(i)
        if a:
            return False
        return True