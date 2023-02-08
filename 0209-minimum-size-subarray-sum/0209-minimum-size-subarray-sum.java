class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int l=0,r=0,s=0;
        int m = Integer.MAX_VALUE;
        while(r<nums.length){
            s+=nums[r++];
            while(s>=target){
                m = Math.min(m,r-l);
                s-=nums[l++];
            }
        }
        return m==Integer.MAX_VALUE ? 0:m;
    }
}