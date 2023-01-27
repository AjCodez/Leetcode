class Solution {
    Trie root = null; // implemenation at the end  
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        root = new Trie('*');
        List<String> ans = new ArrayList<>(); 

        for (String w : words) { 
            insert(root, w.toCharArray()); 
        }

        for (String w : words) { 
            if (search(root, 0, 0, w.toCharArray())) {
                ans.add(w);
            }
        }

        return ans; 
    }

    private boolean search(Trie temp, int found, int idx, char[] word) {
        if (idx == word.length) {
            return found > 1 ? true : false; 
        }

        for (int i=idx; i<word.length; i++) {
            if (!temp.contains(word[i])) return false; 

            temp = temp.get(word[i]);
            if (temp.word) {
                if (search(root, found+1, i+1, word)) return true; 
            }
        }

        return false; 
    }

    private void insert(Trie root, char[] word) {
        Trie temp = root;
        for (int i=0; i<word.length; i++) {
            if (temp.contains(word[i])) {
                temp = temp.get(word[i]);
            } else { 
                temp = temp.insert(word[i]);
            }
        }
        temp.word = true; 
        temp.len = word.length; 
    }


    /** 
     * Trie Node
     */
    private static final class Trie {
        char val; 
        int len = 0; 
        Trie[] children = new Trie[26]; 
        boolean word = false;

        public Trie(char key) { this.val = key; } 
        public boolean contains(char key) { 
            if (children[key-'a'] != null) return true; 
            return false; 
        }
        public Trie insert(char key) {
            if (contains(key)) return children[key-'a']; 
            children[key-'a'] = new Trie(key);
            return children[key-'a']; 
        }
        public Trie get(char key) {
            return children[key-'a']; 
        }
    }
}