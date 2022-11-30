class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for(int a: arr){
            if(hm.containsKey(a)){
                hm.put(a,hm.get(a)+1);
            }
            else{
                hm.put(a,1);
            }
        }
        Set<Integer> s = new HashSet<>(hm.values());
        return s.size()==hm.size();
    }
}