class Solution {
    public int[] nextGreaterElements(int[] nums) {
        Stack<Integer> s = new Stack<>();
        int n=nums.length;
        int [] nums2 = new int[n];
        
        for(int i=2*n-1;i>-1;i--){
            while(true){
                if(s.isEmpty()){
                    nums2[i%n]=-1;
                    s.push(nums[i%n]);
                    break;
                }
                
                if(s.peek()>nums[i%n]){
                    nums2[i%n]=s.peek();
                    s.push(nums[i%n]);
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