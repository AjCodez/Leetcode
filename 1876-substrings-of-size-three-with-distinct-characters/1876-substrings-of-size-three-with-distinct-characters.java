class Solution {
    public int countGoodSubstrings(String s) {
        int k = 3;
	    int c= 0;
        if(s.length()<k) return c;
	    HashMap<Character, Integer> hs = new HashMap<>();
	    for(int i=0;i<k;i++)
	        hs.put(s.charAt(i),hs.getOrDefault(s.charAt(i),0)+1);
	    if(hs.size()==k) c++;
	    int f = 0;
	    for(int i=k;i<s.length();i++){
	        hs.put(s.charAt(f),hs.get(s.charAt(f))-1);
	        if(hs.get(s.charAt(f))==0) hs.remove(s.charAt(f));
	        hs.put(s.charAt(i),hs.getOrDefault(s.charAt(i),0)+1);
	        if(hs.size()==k) c++;
	        f++;
	    }
	    return c;
    }
}