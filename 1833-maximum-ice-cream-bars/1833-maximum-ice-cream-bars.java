class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int bar=0;
        while(bar<costs.length && costs[bar]<=coins)
            coins-=costs[bar++];
        return bar;
    }
}