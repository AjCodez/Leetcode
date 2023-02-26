class Solution {
    public int minDistance(String a, String b) {
        if (a.length() == 0 || b.length() == 0) return a.length() + b.length();
        
        int[][] memo = new int[a.length()][b.length()];
        for (int[] row: memo) Arrays.fill(row, -1);
        return getDistance(a, b, 0, 0, memo);
    }
    
    private int getDistance(String a, String b, int aloc, int bloc, int[][] memo) {
        if (aloc == a.length()) return b.length() - bloc;
        if (bloc == b.length()) return a.length() - aloc;
        if (memo[aloc][bloc] != -1) return memo[aloc][bloc];
        
        int result = 0;
        if (a.charAt(aloc) == b.charAt(bloc)) {
            result = getDistance(a, b, aloc+1, bloc+1, memo);
        } else {
            result = 1 + Math.min(Math.min(getDistance(a, b, aloc+1, bloc, memo), getDistance(a, b, aloc, bloc+1, memo)),
                                  getDistance(a, b, aloc+1, bloc+1, memo));
        }
        return memo[aloc][bloc] = result;
    }
}