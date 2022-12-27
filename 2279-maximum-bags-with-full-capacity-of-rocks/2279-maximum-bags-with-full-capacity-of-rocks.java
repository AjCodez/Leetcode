class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        for(int i=0;i<capacity.length;i++){
            capacity[i]-=rocks[i];
        }
        Arrays.sort(capacity);
        int n=0;
        int i=0;
        while(i<capacity.length && additionalRocks>=capacity[i]){
            additionalRocks-=capacity[i];
            i++;
            n++;
        }
        return n;
    }
}