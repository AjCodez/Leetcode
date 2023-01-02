class Solution {
    public boolean detectCapitalUse(String word) {
        int a=0;
        int b=0;
        for(char c:word.toCharArray()){
            if(Character.isUpperCase(c)) a++;
            else b++;
        }
        if(a==word.length() || b==word.length()) return true;
        if(a==1 && Character.isUpperCase(word.charAt(0))) return true;
        return false;
    }
}