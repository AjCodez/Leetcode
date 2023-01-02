class Solution {
    public boolean detectCapitalUse(String word) {
        int a=0;
        int b=0;
        for(int i=0;i<word.length();i++){
            if(Character.isUpperCase(word.charAt(i))) a++;
            else b++;
        }
        
        if(a==word.length() || b==word.length()) return true;
        if(a==1 && Character.isUpperCase(word.charAt(0))) return true;
        return false;
    }
}