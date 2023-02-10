//{ Driver Code Starts
import java.io.*;
import java.util.*;


class IntArray
{
    public static int[] input(BufferedReader br, int n) throws IOException
    {
        String[] s = br.readLine().trim().split(" ");
        int[] a = new int[n];
        for(int i = 0; i < n; i++)
            a[i] = Integer.parseInt(s[i]);

        return a;
    }

    public static void print(int[] a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }

    public static void print(ArrayList<Integer> a)
    {
        for(int e : a)
            System.out.print(e + " ");
        System.out.println();
    }
}

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            int N;
            N = Integer.parseInt(br.readLine());
            
            
            String S;
            S = br.readLine();
            
            
            int[] P = IntArray.input(br, N);
            
            Solution obj = new Solution();
            int res = obj.getMinimumDays(N, S, P);
            
            out.println(res);
            
        }
        out.close();
    }
}

// } Driver Code Ends


class Solution {
    public static int getMinimumDays(int n, String str, int[] p) {
        
        char a[] = str.toCharArray();
        int i = 0;
        int cnt = countInvalid(n, a);
        if(cnt == 0) return 0;
        for(;i<n;i++){
            if(p[i]<n-1 && a[p[i]] == a[p[i]+1]) cnt--;
            if(p[i]>0 && a[p[i]] == a[p[i]-1]) cnt--; 
            a[p[i]] = '?';
            if(cnt<=0) return i+1;
        }
        return -1;
    }
    public static int countInvalid(int n, char[] a) {
        int res  = 0;
        for(int i = 1;i<n;i++){
            if(a[i] == a[i-1]) res++;
        }
        return res;
    }
}
        
