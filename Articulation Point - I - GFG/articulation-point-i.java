//{ Driver Code Starts
// Initial Template for Java
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int V = Integer.parseInt(s[0]);
            int E = Integer.parseInt(s[1]);
            ArrayList<ArrayList<Integer>>adj = new ArrayList<>();
            for(int i = 0; i < V; i++)
                adj.add(i, new ArrayList<Integer>());
            for(int i = 0; i < E; i++){
                String[] S = br.readLine().trim().split(" ");
                int u = Integer.parseInt(S[0]);
                int v = Integer.parseInt(S[1]);
                adj.get(u).add(v);
                adj.get(v).add(u);
            }
            Solution obj = new Solution();
            ArrayList<Integer>ans = obj.articulationPoints(V, adj);
            for (int i =0 ;i < ans.size (); i++) 
                System.out.print (ans.get (i) + " ");
            System.out.println();
        }
    }
}

// } Driver Code Ends


class Solution
{
    void dfs(ArrayList<ArrayList<Integer>> adj,int i,int parent,
    int toi[],int low[],boolean  vis[],int timer, HashSet<Integer> li){
        
        vis[i]=true;
        toi[i]=low[i]=timer++;
        int child=0;
        for(int it: adj.get(i)){
            if(it==parent)continue;
            if(vis[it]==false){
               dfs(adj,it,i,toi,low,vis,timer,li);
               low[i]=Math.min(low[i],low[it]);
               child++;
               if(low[it]>=toi[i] && parent!=-1){
                   li.add(i);
               }
            }else{
                low[i]=Math.min(low[i],toi[it]);
            }
        }
        if(parent ==-1 && child>1)
        li.add(i);
    }
    public ArrayList<Integer> articulationPoints(int V,ArrayList<ArrayList<Integer>> adj)
    {
        HashSet<Integer> li=new HashSet<>();
        int timer=0;
        int toi[]=new int[V];
        int low[]=new int[V];
        boolean vis[]=new boolean [V];
        
        for(int i=0;i<V;i++){
            if(vis[i]==false){
                dfs(adj,i,-1,toi,low,vis,timer,li);
            }
        }
    ArrayList<Integer> ans=new  ArrayList<>();
       if(li.size()!=0){ for(int a:li){
            ans.add(a);
        }
        Collections.sort(ans);
        return ans;
        
       }else{
           ans.add(-1);
           return ans;
       }
     
    }
}