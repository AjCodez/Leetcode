class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> s = new Stack<Integer>();
        HashMap<Integer, Integer> nums3 = new HashMap<>();
        for(int i=nums2.length-1;i>-1;i--){
            if(s.isEmpty()) nums3.put(nums2[i],-1);
            else{
                while(true){
                    if(s.isEmpty()){
                        nums3.put(nums2[i],-1);
                        break;
                    }
                    if(s.peek()>nums2[i]) {
                        nums3.put(nums2[i],s.peek());
                        break;
                    }
                    else s.pop();
                }
            }
            s.push(nums2[i]);
        }
        for(int i=0;i<nums1.length;i++){
            nums1[i]=nums3.get(nums1[i]);
        }
        return nums1;
    }
}