class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] left = new int[nums.length];
        int [] right = new int[nums.length];
        int l=1;
        int r=1;
        for (int i=0;i<nums.length;i++){
            left[i] = l;
            l*=nums[i];
            right[nums.length-1-i] = r;
            r *= nums[nums.length-1-i];
        }
        for (int i=0;i<nums.length;i++){
            nums[i]=left[i]*right[i];
        }
        return nums;
    }
}