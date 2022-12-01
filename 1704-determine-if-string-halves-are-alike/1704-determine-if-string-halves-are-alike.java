class Solution {
    public boolean halvesAreAlike(String s) {
        int v1=0;
        int v2=0;
        for(int i=0;i<s.length()/2;i++){
            char c1 = s.charAt(i);
            char c2 = s.charAt(s.length()-i-1);
            if (c1=='a'||c1=='e'||c1=='i'||c1=='o'||c1=='u'||c1=='A'||c1=='E'||c1=='I'||c1=='O'||c1=='U') v1++;
            if (c2=='a'||c2=='e'||c2=='i'||c2=='o'||c2=='u'||c2=='A'||c2=='E'||c2=='I'||c2=='O'||c2=='U') v2++;
        }
        if (v1==v2) return true;
        return false;
    }
}