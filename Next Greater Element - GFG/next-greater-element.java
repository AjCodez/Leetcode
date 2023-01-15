//{ Driver Code Starts
/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
    
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine().trim());
		while(t-->0){
		    int n = Integer.parseInt(br.readLine().trim());
		    String inputLine[] = br.readLine().trim().split(" ");
		    long[] arr = new long[n];
		    for(int i=0; i<n; i++)arr[i]=Long.parseLong(inputLine[i]);
		    Solution ob = new Solution();
		    long[] res = ob.nextLargerElement(arr, n);
		    for (int i = 0; i < n; i++) 
		        System.out.print(res[i] + " ");
		    System.out.println();
		}
	}
}




// } Driver Code Ends


// User Function Template for JAVA

class Solution{
    public static long[] nextLargerElement(long[] arr, int n) { 
        Stack<Long> st = new Stack<>();
        long [] arr2 = new long[n];
        for(int i=n-1;i>=0;i--){
            if(st.isEmpty()) arr2[i]=-1;
            else if(st.peek()>arr[i]) arr2[i]=st.peek();
            else{
                while(!st.isEmpty() && st.peek()<=arr[i]) st.pop();
                if(st.isEmpty()) arr2[i]=-1;
                else arr2[i]=st.peek();
            }
            st.push(arr[i]);
        }
        return arr2;
    } 
}