class Solution {
    public int removeElement(int[] nums, int val) {
        int c=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==val) c++;
            else nums[i-c]=nums[i];
        }
        
        return nums.length-c;
    }
}