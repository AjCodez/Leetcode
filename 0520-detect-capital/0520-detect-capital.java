class Solution {
    public boolean detectCapitalUse(String word) {
        int a=0;
        for(int i=0;i<word.length();i++){
            if(Character.isUpperCase(word.charAt(i))) a++;
        }
        
        if(a==word.length() || a==0) return true;
        if(a==1 && Character.isUpperCase(word.charAt(0))) return true;
        return false;
    }
}