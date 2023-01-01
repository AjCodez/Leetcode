class Solution {
    public boolean wordPattern(String pattern, String ss) {
        String[] s = ss.split(" ");
        if(s.length!=pattern.length()) return false;
        HashMap<Character, String> hm = new HashMap<>();
        int i=0;
        for(char ch: pattern.toCharArray()){
            if(hm.containsKey(ch)){
                if(hm.containsValue(s[i]) && hm.get(ch).equals(s[i])) i++;
                else return false;
            }
            else {
                if(hm.containsValue(s[i])) return false;
                else hm.put(ch,s[i++]);
            }  
        }
        return true;
    }
}