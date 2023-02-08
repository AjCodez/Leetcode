class Solution {
    public int jump(int[] nums) {
        int jump = 0;
        int end = 0;
        int curr = 0;
        for(int i=0;i<nums.length-1;i++){
            curr = Math.max(curr,i+nums[i]);
            if(i==end){
                jump++;
                end = curr;
                if(curr == nums.length-1) break;
            }
        }
        return jump;
    }
}