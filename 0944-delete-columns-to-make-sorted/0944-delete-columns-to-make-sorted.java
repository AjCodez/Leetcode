class Solution {
    public int minDeletionSize(String[] strs) {
        int c=0;
        for(int j=0;j<strs[0].length();j++){
            char ch=strs[0].charAt(j);
            for(int i=0;i<strs.length;i++){
                if(ch>strs[i].charAt(j)) {
                    c++;
                    break;
                }
                ch=strs[i].charAt(j);
            }
        }
        return c;
    }
}