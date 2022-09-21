class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int s = 0;
        int [] ans = new int[queries.length];
        for(int i:nums){
            if(i%2==0) s+=i;
        }
        int i=0;
        for(int [] a : queries){
            if (nums[a[1]]%2==0) s-=nums[a[1]];
            nums[a[1]]+=a[0];
            if (nums[a[1]]%2==0) s+=nums[a[1]];
            ans[i++]=s;
        }
        return ans;
    }
}