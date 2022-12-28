class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> prq = new PriorityQueue<>(Collections.reverseOrder());
        for(int i=0;i<piles.length;i++){
            prq.add(piles[i]);
        }
        for(int i=0;i<k;i++){
            int t=prq.poll();
            if(t%2==1) prq.add(((int)t/2)+1);
            else prq.add((int)t/2);
        }
        k=0;
        while(!prq.isEmpty()){
            k+=prq.poll();
        }
        return k;
    }
}