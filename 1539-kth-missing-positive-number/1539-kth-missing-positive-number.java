class Solution {
    public int findKthPositive(int[] arr, int k) {
        int start = 0;
        for(int i=0;i<arr.length;i++){
            if(k > (arr[i]-start-1))
                k -= (arr[i]-start-1);
            else return start+k;
            start = arr[i];
        }
       
        return arr[arr.length-1]+k;
    }
}