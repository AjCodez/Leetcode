class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        PriorityQueue<int[]> can = new PriorityQueue<int[]>((a,b)-> (b[1] - a[1]));
        PriorityQueue<int[]> cannot = new PriorityQueue<int[]>((a,b)-> (a[0] - b[0]));
        int n = capital.length;
        for(int i = 0; i < n; i++){

            if(profits[i] > 0){
                if(w >= capital[i]){
                    can.add(new int[]{capital[i], profits[i]});
                }else{
                    cannot.add(new int[]{capital[i], profits[i]});
                }
            }
        }
        
        while(k-- > 0){
            if(can.size() == 0) break;
            
            w += can.poll()[1];
            
            while(cannot.size() > 0 && w >= cannot.peek()[0]){
                can.add(cannot.poll());
            }
            
        }
        // System.out.println(can.size());
        return w;
    }
}