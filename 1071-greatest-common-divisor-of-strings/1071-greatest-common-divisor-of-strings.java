class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(!(str1+str2).equals(str2+str1)) return "";
        int gcd = 1;
        
        for(int i=1;i<=str1.length()&&i<=str2.length();i++){
            
            if(str1.length()%i==0 && str2.length()%i==0)
                gcd = i;
        }
        
        return str1.substring(0,gcd);
    }
}