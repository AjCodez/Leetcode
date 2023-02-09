//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;

// Position this line where user code will be pasted.

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String s = br.readLine().trim();
            Solution ob = new Solution();
            int ans = ob.maxInstance(s);
            out.println(ans);
        }
        out.close();
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    public int maxInstance(String s) {
        HashMap<Character, Integer> hm  = new HashMap<>();
        
        for(char c:s.toCharArray()) hm.put(c,hm.getOrDefault(c,0)+1);
            
        int m=Integer.MAX_VALUE;
        m = Math.min(m,hm.getOrDefault('b',0));
        m = Math.min(m,hm.getOrDefault('a',0));
        m = Math.min(m,hm.getOrDefault('l',0)/2);
        m = Math.min(m,hm.getOrDefault('o',0)/2);
        m = Math.min(m,hm.getOrDefault('n',0));
        return m;
    }
}