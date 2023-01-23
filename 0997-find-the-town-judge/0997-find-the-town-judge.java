class Solution {
    public int findJudge(int n, int[][] trust) {
        // int[][] mat = new int[n][n];
        // for(int [] i:trust){
        //     mat[i[0]-1][i[1]-1]=1;
        // }
        // int c=-1;
        // for(int i=0;i<n;i++){
        //     boolean f = true;
        //     for(int j=0;j<n;j++){
        //         if(mat[i][j]==1){ f=false;
        //         break;}
        //     }
        //     if(f){
        //         if(c==-1) c=i;
        //         else return -1;
        //     }
        // }
        // if(c==-1) return -1;
        // for(int i=0;i<n;i++){
        //     if(i!=c)
        //         if(mat[i][c]==0) return -1;
        // }
        // return c+1;
        int[] count = new int[n];
        for (int[] t: trust) {
            count[t[0]-1]--;
            count[t[1]-1]++;
        }
        for (int i = 0; i < n; i++) {
            if (count[i] == n - 1) return i+1;
        }
        return -1;
    }
}