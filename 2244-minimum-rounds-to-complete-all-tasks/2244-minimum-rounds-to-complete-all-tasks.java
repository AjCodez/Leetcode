class Solution {
    public int minimumRounds(int[] tasks) {
        int count=0;
        HashMap<Integer, Integer> mp = new HashMap<>();
        for(int i:tasks){
            mp.put(i,mp.getOrDefault(i,0)+1);
        }
        for(int i:mp.values()){
            if(i==1) return -1;
            count +=(i+2)/3;
        }
        
        return count;
    }
}