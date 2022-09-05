class Solution {
    
    private static void nextPermutation1(int[] arr) {
		int a = 0;
		for (int i = arr.length - 2; i >= 0; i--) {
			if (arr[i] < arr[i + 1]) {
				a = i;
				break;
			}
		}
		int b = 0;
		for (int i = arr.length - 1; i > a; i--) {
			if (arr[i] > arr[a]) {
				b = i;
				break;
			}
		}
		if (a == 0 && b == 0) {
			rangeReverse(arr, 0, arr.length - 1);
			return;
		}
		int temp = arr[a];
		arr[a] = arr[b];
		arr[b] = temp;
		rangeReverse(arr, a + 1, arr.length - 1);
	}
    
    private static void rangeReverse(int[] arr, int i, int j) {
		while (i < j) {
			int temp = arr[i];
			arr[i] = arr[j];
			arr[j] = temp;
			i++;
			j--;
		}
	}
    
    public void nextPermutation(int[] nums) {
        nextPermutation1(nums);
    }
}