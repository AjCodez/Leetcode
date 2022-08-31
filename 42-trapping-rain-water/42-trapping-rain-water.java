class Solution {
    public int trap(int[] height) {
        int [] arr1 = new int[height.length];
        int [] arr2 = new int[height.length];
        int max = 0;
        for ( int i=0;i<height.length; i++){
            arr1[i]=Math.max(height[i],max);
            max=Math.max(height[i],max);
        }
        max=0;
        for ( int i=height.length-1;i>-1; i--){
            arr2[i]=Math.max(height[i],max);
            max=Math.max(height[i],max);
        }
        int water=0;
        for(int i=0;i<height.length;i++){
            water+=Math.min(arr1[i],arr2[i])-height[i];
        }
        return water;
    }
}