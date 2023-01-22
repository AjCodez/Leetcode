class Solution {
    List<List<String>> res = new ArrayList<>();
    List<String> arr = new ArrayList<>();
    public List<List<String>> partition(String s) {
        rec(s,0);
        return res;
    }
    
    public void rec(String s, int n){
        if(n>=s.length())
            res.add(new ArrayList(arr));
        for(int i=n;i<s.length();i++){
            if(isPalindrome(s,n,i)){
                arr.add(s.substring(n,i+1));
                rec(s,i+1);
                arr.remove(arr.size()-1);
            }
        }
    }
    
    public boolean isPalindrome(String s, int l, int r){
        while(l<r){
            if(s.charAt(l)!=s.charAt(r)) return false;
            l++;r--;
        }
        return true;
    }
}