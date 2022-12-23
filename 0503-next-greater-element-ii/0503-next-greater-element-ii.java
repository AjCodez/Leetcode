class Solution {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> s = new Stack<>();
        int [] nums2 = new int[nums.length];
        for(int i=2*nums.length-1;i>-1;i--){
            while(true){
                if(s.isEmpty()){
                    nums2[i%nums.length]=-1;
                    s.push(nums[i%nums.length]);
                    break;
                }
                if(s.peek()>nums[i%nums.length]){
                    nums2[i%nums.length]=s.peek();
                    s.push(nums[i%nums.length]);
                    break;
                }
                else{
                    s.pop();
                }
            }
        }
        return nums2;
    }
}