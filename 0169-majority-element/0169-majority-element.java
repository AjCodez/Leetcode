class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();
        for(int i:nums){
            if(hm.containsKey(i)) hm.put(i,hm.get(i)+1);
            else hm.put(i,1);
        }
        for(int i:hm.keySet()){
            if(hm.get(i)>nums.length/2) return i;
        }
        return -1;
    }
}