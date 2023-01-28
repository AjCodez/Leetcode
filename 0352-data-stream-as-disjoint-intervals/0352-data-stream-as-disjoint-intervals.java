public class SummaryRanges {
    TreeSet<int[]> set;
    public SummaryRanges() {
        set = new TreeSet<>((a,b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0]);
    }

    public void addNum(int val) {
        int[] interval = new int[]{val, val};
        if(set.contains(interval)) return;
        int[] high = set.higher(interval);
        int[] low = set.lower(interval);

        if(high != null && high[0] == val + 1 && low != null && low[1] == val - 1) {
            high[0] = low[0];
            set.remove(low);
        }
        else if(high != null && high[0] == val + 1)
            high[0]--;
        else if(low != null && low[1] == val - 1)
            low[1]++;
        else if((high != null && high[0] == val) || (low != null && low[1] >= val && low[0] <= val))
            return;
        else      
            set.add(interval);
    }

    public int[][] getIntervals() {
        List<int[]> list = new ArrayList<>();
        for(int[] interval : set) list.add(interval);
        return list.toArray(new int[0][]);
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(value);
 * int[][] param_2 = obj.getIntervals();
 */