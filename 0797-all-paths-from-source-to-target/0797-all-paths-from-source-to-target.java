class Solution {
    private static List<List<Integer>> l;
    private static void dfs(int curr, List<Integer> ll, int[][] graph){
        if(curr==graph.length-1){
            l.add(new ArrayList<>(ll));
            return;
        }
        for(int i:graph[curr]){
            ll.add(i);
            dfs(i,ll,graph);
            ll.remove(ll.size()-1);
        }
    }
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        l=new ArrayList();
        List<Integer> ll = new ArrayList();
        ll.add(0);
        dfs(0,ll,graph);
        return l;
    }
}