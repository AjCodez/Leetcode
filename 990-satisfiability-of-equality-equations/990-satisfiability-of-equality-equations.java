class Solution {
    public boolean equationsPossible(String[] equations) {
        int[] parent = new int[26];
    
    for (int i = 0; i < 26; i++) {
        parent[i] = i;
    }
  
    
    //Equality condition
    for (String s: equations) {
        if (s.charAt(1) == '=') {
        
            int s1 = findParent(s.charAt(0)-'a', parent);
            int s2 = findParent(s.charAt(3)-'a', parent);
            
            if (s1 != s2) {
                parent[s2] = s1;
            }
        }
        
    }
    
    for (String s : equations) {
        if(s.charAt(1) == '!') {
            int s1 = findParent(s.charAt(0)-'a', parent);
            int s2 = findParent(s.charAt(3)-'a', parent);
            
            if (s1 == s2) {
                return false;
            }
        }
    }
    
    return true;
}

private int findParent(int index, int[] parent) {
    if (index == parent[index]) {
        return index;
    }
    return findParent(parent[index], parent);
}
}