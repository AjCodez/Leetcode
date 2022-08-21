class Solution:
    def corresponds(self, stamp, target, idx):
            for s in stamp:
                if s == target[idx] or target[idx] == '?': 
                    idx += 1
                else:  
                    return False
            return True
                
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        
        n = len(stamp)
        m = len(target)
        
        if n == m:
            if stamp == target: 
                return [0]
            return []
        
        initial = '?'*m
        res = []
        
        updated = True
        while updated:
            
            updated = False
            l, r = 0, n-1
            while r < m:
                if '?'*n != target[l:r+1] and self.corresponds(stamp, target,l):
                    res.append(l)
                    target = target[:l] + "?"*n + target[l+n:]
                    updated = True
                
                l += 1; r += 1
                
            if target == initial:
                return res[::-1]
            
        return []