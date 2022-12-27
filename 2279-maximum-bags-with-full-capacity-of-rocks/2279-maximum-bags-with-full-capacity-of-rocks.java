class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        for(int i=0;i<capacity.length;i++){
            capacity[i]-=rocks[i];
        }
        Arrays.sort(capacity);
        int n=0;
        while(n<capacity.length && additionalRocks>=capacity[n]){
            additionalRocks-=capacity[n];
            n++;
        }
        return n;
    }
}